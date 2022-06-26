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

GridWorldGenerator.generate_data(output_dir=PROBLEM_STATE_DSET_DIR)
FFXSolver.solve_problem_dir(
    domain_file=DOMAIN_FILE,
    problem_dir=PROBLEM_STATE_DSET_DIR,
    output_dir=PROBLEM_SOLUTION_DIR,
)


def write_db(f, state, plan):
    # f.write(state.mln(cap_args=True))
    for index, s in enumerate(plan["steps"]):
        p = Predicate(**s["predicate"])
        f.write("\n" + p.mln(cap_args=True))
        f.write(s.mln(cap_args=True, extra_args=["0"]))

        state.perform_action(p)

        for pr in state.latest_removed:
            f.write("\n" + pr.mln(cap_args=True, extra_args=["-1"]))
        for pr in state.latest_added:
            f.write("\n" + pr.mln(cap_args=True, extra_args=["1"]))

        if index < len(plan["steps"]) - 1:
            f.write("\n--- ")


domain = "grid"
parsed = parse_pddl("../domains/" + domain + ".pddl")
mln_database = "mln_db.mln"
fl = open(mln_database, "w")
a = 1
for i in range(1, 100):
    try:
        state = State(parsed)
        problem = parse_state(domain, "state_" + str(i))
        state.set_init_state(problem["init"])
        plan = parse_plan(domain, "state_" + str(i))
        print(len(plan["steps"]))
        write_db(fl, state, plan)
        fl.write("\n---\n")
        a += 1
    except Exception:
        continue
    # except Exception as e:
    #     print(str(e),i,state,problem)
    #     exit()
fl.close()
print(a)
