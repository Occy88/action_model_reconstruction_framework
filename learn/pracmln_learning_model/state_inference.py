from domain.simulator import Predicate, Action, State
from itertools import chain
from opensource.pracmln.pracmln_patched import MLN
from opensource.pracmln.pracmln_patched import Database as DB
from matplotlib import pyplot as plt
import json
import numpy as np
import random


class Database:
    def __init__(
            self, action: Predicate, state: set, pos_effects: set, neg_effects: set
    ):
        self.action = action
        self.state = state
        self.pos_effects = pos_effects
        self.neg_effects = neg_effects
        # precompute s why not...
        self._action_related_predicates = None



    def noise(self, prob):
        """
        removes percentage of predicates from database
        Args:
            prob: probability predicate is removed 0->1

        Returns:

        """

        def p(plist):
            return int(len(plist) * (1 - prob))

        def samp(plist):
            return random.sample(plist, p(plist))

        print("=========[ noise: ]==============")
        print(len(self.state))
        self.state = samp(self.state)
        print(len(self.state))
        self.pos_effects = samp(self.pos_effects)
        self.neg_effects = samp(self.neg_effects)

    def sys_noise(self, p_name, prob):
        def p(pset):
            rep = set()
            for i, val in enumerate(pset):
                p = random.random()  # nosec
                val.arg_types = Predicate.matching_as_variables(self.action, val)
                # nm = val.mln_type()
                if val.mln_type() == p_name:
                    if p < prob:
                        print("ADDED - (System noise)")
                        rep.add(val)
                else:
                    rep.add(val)
            return rep

        self.state = p(self.state)
        self.neg_effects = p(self.neg_effects)
        self.pos_effects = p(self.pos_effects)

    @property
    def action_related_predicates(self):
        """
        returns all predicates that have an argument that is present in
        the action's argument.
        Returns:
        """
        s = set()
        for p in chain(self.state, self.pos_effects, self.neg_effects):
            # TODO exclusion should not be limited to on? thi is to be discussed
            # s.add(p)
            if (
                    len(self.action.arg_set.intersection(p.arg_set)) > 0
                    and len(p.arg_set.difference(self.action.arg_set)) < 2
            ):
                s.add(p)

        return s

    def mln_db(self):
        a = self.action.mln()
        p = ""
        for pr in chain(self.state, self.neg_effects, self.pos_effects):
            p += pr.mln() + "\n"
        return a + "\n" + p

    @staticmethod
    def parse_db(db: str):
        p_str = db.split("\n")
        p_p = []
        for p in p_str:
            # remove comments
            p = p.split("//")[0]
            # avoid empty lines, not nice for now but whatever.
            if len(p) < 2:
                continue
            p_p.append(Predicate.from_str(p))
        pos_effects = set()
        neg_effects = set()
        state = set()
        action = ""
        for p in p_p:
            if p.args[-1] == "0":
                state.add(p)
            elif p.args[-1] == "1":
                pos_effects.add(p)
            elif p.args[-1] == "-1":
                neg_effects.add(p)
            else:
                if not action == "":
                    raise Exception(
                        "Multiple actions in database: ", p.name, action.name
                    )
                action = p
        return Database(p_p[0], state, pos_effects, neg_effects)


def center(A):
    if type(A) != np.ndarray:
        A = np.array(A)
    return A - ((np.max(A) - np.min(A)) / 2)


class StateInfrence:
    def __init__(self, predicate_file):
        self.predicate_file = predicate_file
        # set of markov logic networks
        self.action_dbs = dict()
        self.action_mln = dict()
        self.action_weights = dict()
        self.action_rejected_weights = dict()
        self.action_pending_weights = dict()
        self.actions = dict()
        self.logic = "FirstOrderLogic"
        self.grammar = "StandardGrammar"
        self.method = "pseudo-log-likelihood"
        self.data_for_graph = dict()
        self.db_run = dict()
        self.dbs = []
        pass

    def process_database(self, db: Database):
        self.db = db
        self._new_action_process()

    def update_mln(self):
        print("UPDATING MLN")
        action = self.db.action
        # if action.name not in self.action_mln:

        predicates = open(self.predicate_file).read() + "\n\n// formulas: \n"
        weights = self.gen_weights(action)
        f = open("tmp.mln", "w")
        f.write(predicates + weights)
        f.close()
        if action.name in self.action_mln:
            m = self.action_mln[action.name]
            existing_weights = set()
            print(m.predicates)
            print("M length: ", print(len(m.formulas)))
            print(self._unmodified_predicates)
            for i, form in enumerate(m.weighted_formulas):
                predicate_key = str(form.children[1])
                existing_weights.add(predicate_key)
            for k, w in self.action_weights[action.name].items():
                form_name = w.mln_type()
                if form_name not in existing_weights:
                    existing_weights.add(form_name)
                    m.formula(action.mln_type() + " => " + form_name)
            m_parse = MLN(self.logic, self.grammar, mlnfile="tmp.mln")
            print(len(m.weights), len(m.formulas))
        else:
            m = MLN(self.logic, self.grammar, mlnfile="tmp.mln")
            m_parse = m
            self._unmodified_predicates = m.predicates

        # m.weights[1]=1
        # m.weights[2]=10
        # else:
        #     m = self.action_mln[action.name]
        open("tmp_db.mln", "w").write(self.db.mln_db())
        try:
            db = DB.load(m, "tmp_db.mln")
        except Exception as e:
            db = DB.load(m_parse, "tmp_db.mln")
            print(e)
        print(db[0].evidence)

        self.action_dbs[self.db.action.name].append(db)
        res = m.learn_iter(db)
        # r = MLNQuery(mln=res, db=db[0]).run()
        # prev_weights = list(map(lambda a: a.weight, self.action_weights[self.db.action.name].values()))

        # weights_std = center(res.weights)
        weights_std = res.weights
        print(weights_std)
        res.write()
        # weights_std = weights_std[:-len(prev_weights)]
        for i, form in enumerate(res.weighted_formulas):
            predicate_key = str(form.children[1])
            # self.action_weights[self.db.action.name][predicate_key].weight += res.weights[i]
            self.action_weights[self.db.action.name][
                predicate_key
            ].weight = res.weights[i]
            # res.weights[i] += self.action_weights[self.db.action.name][predicate_key].weight

        # print(res.weights)
        # res.weights[3] = 2
        self.action_mln[action.name] = m
        return m

    # def gen_predicates(self,action:Predicate):def preprocessor(X):
    #     return preprocess_images(X, (32, 32, 3), clean_img)
    #     preds = Predicate.unique_by_name(self.action_weights[action.name])
    #     p_str=''
    #     for p in preds:
    #         p_str+=p.mln_type()
    def prune_weights(self, action_name, threshold):
        """
        Prunes weights, (adds them to rejected weights), this is to speed up
        training if some weights go below a given threshold.
        Args:
            threshold:
        Returns: None
        """
        weights = self.action_weights[action_name]
        accepted = dict()
        # accepted_w=[]
        for p_name, p in weights.items():
            if p.weight < threshold:
                self.action_rejected_weights[action_name][p.mln_type()] = p
            elif p.mln_type() not in self.action_rejected_weights[action_name]:
                accepted[p.mln_type()] = p
                # accepted_w.append(p.weight)
        self.action_weights[action_name] = accepted

    def insert_weights(self):
        db = self.db
        relevant_weights = db.action_related_predicates
        # existing_weights=self.action_weights[db.action]
        # existing_rejected_weidghts=self.action_rejected_weights[db.action]
        db.action.arg_types = Predicate.matching_as_variables(db.action, db.action)

        if db.action.name not in self.action_weights:
            self.action_dbs[db.action.name] = []
            self.action_weights[db.action.name] = dict()
            self.action_pending_weights[db.action.name] = dict()
            self.action_rejected_weights[db.action.name] = dict()
            self.actions[db.action.name] = db.action
        for w in relevant_weights:
            w.arg_types = Predicate.matching_as_variables(db.action, w)
            if (
                    w.mln_type() in self.action_rejected_weights[db.action.name]
                    or w.mln_type() in self.action_weights[db.action.name]
            ):
                continue
            else:
                self.action_weights[db.action.name][w.mln_type()] = w

    def gen_weights(self, action: Predicate):
        s = ""
        for k, w in self.action_weights[action.name].items():
            s += (
                    str(w.weight)
                    + "    "
                    + action.mln_type()
                    + " => "
                    + w.mln_type()
                    + "\n"
            )
        # print(s)
        return s

    def _new_action_process(self):
        """
        Check if the action already exists, add it if it doesn't,
        find all relevant preconditions add them to the mln if there are new ones
        check for contradictions -> split into two mlns if there are

        Args:

        Returns:

        """
        self.insert_weights()  # CREATES MLN'S
        self.update_mln()
        self.update_data_for_graph()

    def update_data_for_graph(self):
        """
        data is in the shape:
        action name:
        predicate_name weight run
        predicate_name weight run
        ...
        action name:
        predicate_name weight run
        predicate_name weight run
        ...
        """

        a = self.db.action.name
        if a not in self.data_for_graph:
            self.db_run[a] = 0
            self.data_for_graph[a] = dict()
        else:
            self.db_run[a] += 1
        for k, p in self.action_weights[a].items():
            if k not in self.data_for_graph[a]:
                # fill all missed runs with 'NaN' value.
                self.data_for_graph[a][k] = [np.nan] * self.db_run[a]
            if len(self.data_for_graph[a][k]) > 100:
                print("longer: ", k, "  ", len(self.data_for_graph[a][k]))
                pass
            self.data_for_graph[a][k].append(p.weight)

        for k, p in self.action_rejected_weights[a].items():
            if len(self.data_for_graph[a][k]) > 100:
                print("longer-nan: ", k, "  ", len(self.data_for_graph[a][k]))
                pass
            self.data_for_graph[a][k].append(np.nan)

    def save_data_for_graphing(self):
        f = open("graph_data", "w+")
        f.write(json.dumps(self.data_for_graph))

    @staticmethod
    def count_nan(li):
        t = 0
        for v in li:
            if np.isnan(v):
                t += 1
        return t

    @staticmethod
    def plot():
        d = json.loads(open("graph_data", "r").read())
        print(d)
        for k in d:
            a = d[k]
            for key, val in a.items():
                if len(val) > 100:
                    print("-----------------")
                    print(len(val), key)
                label = key if StateInfrence.count_nan(val) < len(val) * 0.5 else None
                plt.plot(list(range(0, len(val))), val, "o-", label=label)
                # break
            plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left", fontsize="xx-small")
            print(k)
            plt.title(k)
            plt.subplots_adjust(right=0.7, top=0.8)
            plt.savefig(k + "graph.png", dpi=600)
            plt.show()
            # break
