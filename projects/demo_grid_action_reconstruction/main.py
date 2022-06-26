import os

from learn.pracmln_learning_model import PracmlnLearningModel
from generator.generator import GridWorldGenerator
from parser.ff_to_action import FFToActionParser
from solvers.solvers import FFXSolver
from pddl_parser.pddl_22_parser.pddl_parser import parse_pddl

from generator.state_to_json import parse_state
from learn.pracmln_learning_model.state_inference import Predicate
from learn.pracmln_learning_model.state_inference import State
from solvers.ffx.plan_to_json import parse_plan

BASE_PATH = os.path.normpath(f"{os.getcwd()}/..")

PROJECT_DIR = os.path.dirname(__file__)
DATA_DIR = f"{PROJECT_DIR}/data"
PROBLEM_STATE_DSET_DIR = f"{DATA_DIR}/problem_states"
DOMAIN_FILE = f"{PROJECT_DIR}/grid.pddl"
PROBLEM_SOLUTION_DIR = f"{DATA_DIR}/problem_solutions"
MLN_DATABASE = f'{DATA_DIR}/mln_db.mln'
GridWorldGenerator.generate_data(output_dir=PROBLEM_STATE_DSET_DIR)
FFXSolver.solve_problem_dir(
    domain_file=DOMAIN_FILE,
    problem_dir=PROBLEM_STATE_DSET_DIR,
    output_dir=PROBLEM_SOLUTION_DIR,
)


# convert solutions to MLN databases
def write_db(f, state, plan):
    # f.write(state.mln(cap_args=True))
    for index, s in enumerate(plan["steps"]):
        p = Predicate(**s["predicate"])
        f.write("\n" + p.mln(cap_args=True))
        f.write(state.mln(cap_args=True, extra_args=["0"]))

        state.perform_action(p)

        for pr in state.latest_removed:
            f.write("\n" + pr.mln(cap_args=True, extra_args=["-1"]))
        for pr in state.latest_added:
            f.write("\n" + pr.mln(cap_args=True, extra_args=["1"]))

        if index < len(plan["steps"]) - 1:
            f.write("\n--- ")


def write_dbs():
    parsed = parse_pddl(DOMAIN_FILE)
    fl = open(MLN_DATABASE, "w+")
    a = 1
    for i in range(1, 100):
        try:
            state = State(parsed)
            problem = parse_state(f'{PROBLEM_STATE_DSET_DIR}/state_{i}')
            state.set_init_state(problem["init"])
            plan = parse_plan(f'{PROBLEM_SOLUTION_DIR}/state_{i}')
            print(len(plan["steps"]))
            write_db(fl, state, plan)
            fl.write("\n---\n")
            a += 1
        except Exception as e:
            continue
        # except Exception as e:
        #     print(str(e),i,state,problem)
        #     exit()
    fl.close()
    print(a)


write_dbs()
