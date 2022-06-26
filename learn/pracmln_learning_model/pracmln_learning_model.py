import os
import random

from learn import LearningModelInterface

# from opensource.pracmln.pracmln_patched.mln.database import Database as DB
from .state_inference import Database as DB
from .state_inference import StateInfrence


class PracmlnLearningModel(LearningModelInterface):
    def __init__(
        self,
        mln_database_path: str,
        domain_p_decs_path: str,
    ):
        # state.perform_action('move-b-to-t', ('b9', 'b4'))
        mln_database = "../data/mln/mln_db.mln"
        self.domain = "grid"
        num_databases = 25
        print("Loading database file: ")
        databases = open(mln_database).read()
        databases = databases.strip("\n").strip(" ").strip("---").split("---")
        random.shuffle(databases)
        databases = databases[:num_databases]
        self.d_processed = []
        print("Processing databases")
        for i, d in enumerate(databases):
            print(i / len(databases))
            # cut out any blank databases.
            if len(d) < 20:
                pass
            self.d_processed.append(DB.parse_db(d))
        print("initiating state inference")
        self.state_inference: StateInfrence = StateInfrence(
            os.path.normpath(os.path.join(os.getcwd(), domain_p_decs_path))
        )
        ...

    def train(self):

        print("Initiating learning:")
        opt_tracker = dict()
        for i, d in enumerate(self.d_processed):
            if d.action.name == "unlock":
                continue
            if d.action.name not in opt_tracker:
                opt_tracker[d.action.name] = 0
            # systematic noise on move function
            if d.action.name == "move":
                if opt_tracker[d.action.name] >= 1:
                    # d.noise(0.3)
                    d.sys_noise("conn(v0,v1,0)", 0.5)

            else:
                continue
            #     pass

            print(
                f"=========[ processing db: {d.action.name} {i} / {len(self.d_processed)} ]==========="
            )
            print(i / len(self.d_processed))
            self.state_inference.process_database(d)

            # s.update_data_for_graph(i)
            # if opt_tracker[d.action.name] % 5 and not opt_tracker[d.action.name] == 0:
            #     s.prune_weights(d.action.name,2)
            opt_tracker[d.action.name] += 1
            self.state_inference.save_data_for_graphing()

        s = StateInfrence(os.getcwd() + "/" + self.domain + "_p_decs.txt")
        self.state_inference.plot()
        print("writing results")
        # for k in iter(s.action_weights):
        #     print("============[ ", k, " ]============")
        #
        #     for i, p in enumerate(s.action_weights[k]):
        #         print(p.weight, "    ", s.actions[k].mln_type(), " => ", p.mln_type())
        # print("done")
        # result=mln.learn(db)
        #
        # result.write(pr())
        #
        # result.write(results)
