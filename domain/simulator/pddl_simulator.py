import copy

from typing import List, Set


class Predicate:
    def __init__(self, name="", args="9", arg_types="number"):
        self.name = name
        self.args = args
        self.arg_set = set(args)
        self.arg_types = arg_types
        self.weight = 0.0

    def _get_mln_str(self, args_to_use, cap_args, extra_args: List = None):
        if extra_args is None:
            extra_args = []
        args = copy.copy(args_to_use)
        if cap_args:
            args = list(map(lambda x: x.capitalize(), self.args))
        args += extra_args
        return self.name + "(" + ",".join(args) + ")"

    def mln(self, cap_args=False, extra_args: List = None):
        return self._get_mln_str(self.args, cap_args, extra_args)

    def mln_type(self, cap_args=False, extra_args: List = None):
        return self._get_mln_str(self.arg_types, cap_args, extra_args)

    def __copy__(self):
        return Predicate(self.name, self.args)

    def __hash__(self):
        return hash(self.name + str(self.args))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __str__(self):
        return " ".join((self.name, ": ", " ".join(self.args)))

    def get_property_hash(self, properties):
        """
        Concatenates multiple properties of object
        returns hash of resulting string
        Args:
            properties:
        Returns:

        """
        p_vals = ""
        for p in properties:
            p_vals += str(getattr(self, p))
        return hash(p_vals)

    @staticmethod
    def from_str(p_str):
        sp = p_str.split("(")
        args = sp[1]
        args = args.strip(")").replace(" ", "").split(",")
        return Predicate(sp[0], args)

    @staticmethod
    def exists_in_list_by_properties(predicate, predicate_list, properties):
        """Tests if there is a predicate with the same name in a list of predicates

        :param predicate:
        :param predicate_list:
        :param properties:
        :return:
        """
        for p in predicate_list:
            if p.get_property_hash(properties) == predicate.get_property_hash(
                properties
            ):
                return True
        return False

    @staticmethod
    def match_arguments(p_parent, p_child):
        """
        returns list of of indices of childs arguments present in the parent
        -1 if no match is found.
        e.g.
        p_parent.args=[a,b,c,d]
        p_child.args=[c,a,z]
        => [2,0,-1]
        Args:
            p_parent:
            p_child:

        Returns:
        """
        matching_list = []
        for p in p_child.args:
            try:
                matching_list.append(p_parent.args.index(p))
            except ValueError:
                matching_list.append(-1)
        return matching_list

    @staticmethod
    def matching_as_variables(p_parent, p_child):
        """
        uses match_arguments, converts to variable names (V1 V2)
        for any -1's for now we simply set them as the value of the argument
        assume it is not a variable for now.
        Args:
            p_parent:
            p_child:

        Returns:
        """
        matching_i = Predicate.match_arguments(p_parent, p_child)
        matching_v = []
        for i, v in enumerate(matching_i):
            if int(v) < 0:
                matching_v.append(p_child.args[i])
            else:
                matching_v.append("v" + str(v))
        return matching_v

    @staticmethod
    def unique_by_name(predicate_list):
        """
        returns unique set of predicates from list by name.
        Args:
            predicate_list:

        Returns:
        """
        unique_names = set()
        unique_preds = set()
        for p in predicate_list:
            if p.name not in unique_names:
                unique_preds.add(p)
                unique_names.add(p.name)
        return unique_preds


class Action:
    arg_locations = dict()

    def __init__(self, name="", args="", precondition="", effect=dict):
        self.name = name
        self.args = args
        self._set_arg_locations()
        self.precondition = precondition
        self.pos = self._get_predicates(effect["positive"])
        self.neg = self._get_predicates(effect["negative"])

    def _set_arg_locations(self):
        self.arg_locations = dict()
        for i, a in enumerate(self.args):
            self.arg_locations[a] = i

    def get_pos_list(self, args):
        return self.get_list(self.pos, args)

    def get_neg_list(self, args):
        return self.get_list(self.neg, args)

    def get_list(self, eff_list, args) -> Set[Predicate]:
        """
        applies predicate on the positive/neg effects of an action
        and returns the set of predicates that are generated by said action.
        :param eff_list:
        :param args:
        :return:
        """
        if len(args) < len(self.args):
            raise Exception(
                "Arguments do not match Action footprint,\n expecting: "
                + str(self.args)
                + " | got: "
                + str(args)
            )
        return_predicates = set()

        for p in eff_list:
            pc = p.__copy__()
            pc.args = list(
                map(
                    lambda x: args[x],
                    list(map(lambda y: self.arg_locations[y], p.args)),
                )
            )
            return_predicates.add(pc)
        return return_predicates

    def _get_predicates(self, effect):
        predicates = []
        for p in effect:
            predicates.append(Predicate(**p))
        return predicates

    def __hash__(self):
        return hash(str(self.name) + str(self.args))


class State:
    actions = dict()

    def __init__(self, state):
        self._set_actions(state["actions"])
        self.state = set()
        self.latest_removed = set()
        self.latest_added = set()
        # self.latest_added=set()

    def perform_action(self, p: Predicate):
        # print(self)
        pos = self.actions[p.name].get_pos_list(p.args)
        self.state = self.state | pos
        self.latest_added = pos
        neg = self.actions[p.name].get_neg_list(p.args)
        self.latest_removed = neg
        self.state = self.state - neg

    def _set_actions(self, actions):
        for a in actions:
            self.actions[a["name"]] = Action(**a)

    def set_init_state(self, predicate_json):
        for p in predicate_json:
            self.state.add(Predicate(**p))

    def mln(self, cap_args=False, extra_args: List = None):
        s = ""
        for p in self.state:
            s += "\n" + p.mln(cap_args=cap_args, extra_args=extra_args)
        return s

    def __str__(self):
        for p in self.state:
            return str(p)


#
#
# def update_mln():
#     print("UPDATING MLN")
#     logic = "FirstOrderLogic"
#     grammar = "StandardGrammar"
#     # method = "pseudo-log-likelihood"
#     m = MLN(logic, grammar, mlnfile="../tmp1.mln")
#     # m.weights[1]=1
#     # m.weights[2]=10
#     # else:
#     #     m = self.action_mln[action.name]
#     # db_both = DB.load(m, "../tmp_db3.mln")
#     # db_1 = DB.load(m, "../tmp_db1.mln")
#     db_2 = DB.load(m, "../tmp_db2.mln")
#     # a = m.learn(db_both)
#     # print(a.weights)
#     # b = m.learn_iter(db_1)
#     c = getattr(m, "learn_iter")(db_2)
#     print(
#         "target: ",
#         [
#             5.3619451781468195,
#             2.8782336808825564,
#             -0.7494174682462591,
#             3.793552188739899,
#             3.5295832607294213,
#             13.918149709704712,
#             2.878233680882602,
#             13.918149709704519,
#             5.884279775032551,
#         ],
#     )
#     print("value: ", c.weights)
#
# # update_mln()
# # action_dbs[self.db.action.name].append(db)
# # res = m.learn(self.action_dbs['move'])
# # # r = MLNQuery(mln=res, db=db[0]).run()
# # # prev_weights = list(map(lambda a: a.weight, self.action_weights[self.db.action.name].values()))
# #
# # # weights_std = center(res.weights)
# # weights_std = res.weights
# # # weights_std = weights_std[:-len(prev_weights)]
# # for i, form in enumerate(res.weighted_formulas):
# #     predicate_key = str(form.children[1])
# #     self.action_weights[self.db.action.name][predicate_key].weight += weights_std[i]
# #     # res.weights[i] += self.action_weights[self.db.action.name][predicate_key].weight