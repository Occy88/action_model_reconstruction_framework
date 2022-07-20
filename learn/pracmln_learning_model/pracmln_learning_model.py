import os
import random

from learn import LearningModelInterface
# from opensource.pracmln.pracmln_patched.mln.database import Database as DB
from .state_inference import Database as DB
from .state_inference import StateInfrence
from collections import defaultdict
from .utils import load_dbs


class PracmlnLearningModel(LearningModelInterface):
    def __init__(
            self,
            mln_database_path: str,
            domain_p_decs_path: str,
            max_databases=25,
    ):
        # load dataset
        databases = load_dbs(mln_database_path)
        random.shuffle(databases)
        databases = databases[:max_databases]
        self.dataset = [DB.parse_db(db) for db in databases]

        # initiate pracmln learner
        self.state_inference: StateInfrence = StateInfrence(
            os.path.normpath(os.path.join(os.getcwd(), domain_p_decs_path))
        )

    def train(self):
        # track how many databases were added for each action being learnt
        opt_tracker = defaultdict(int)
        for i, d in enumerate(self.dataset):
            # systematic noise on move function (to be moved to preprocessing)
            if d.action.name == "move":
                if opt_tracker[d.action.name] >= 1:
                    # d.noise(0.3)
                    d.sys_noise("conn(v0,v1,0)", 0.5)
            # pass data through Markov Logic Network
            self.state_inference.process_database(d)
            opt_tracker[d.action.name] += 1
            # write data for metrics, remove for speed & space use reduction
            self.state_inference.save_data_for_graphing()
        # plot learning confidence results.
        self.state_inference.plot()
