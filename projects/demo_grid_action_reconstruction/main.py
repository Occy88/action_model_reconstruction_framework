import os

from generator.generator import GridWorldGenerator
from solvers.solvers import FFXSolver
from projects.demo_grid_action_reconstruction.states_to_db import write_dbs
from learn.pracmln_learning_model import PracmlnLearningModel
from learn.pracmln_learning_model.mln_playground import MLNDeclarationGenerator

BASE_PATH = os.path.normpath(f"{os.getcwd()}/..")

PROJECT_DIR = os.path.dirname(__file__)
DATA_DIR = f"{PROJECT_DIR}/data"
PROBLEM_STATE_DSET_DIR = f"{DATA_DIR}/problem_states"
DOMAIN_FILE = f"{PROJECT_DIR}/grid.pddl"
PROBLEM_SOLUTION_DIR = f"{DATA_DIR}/problem_solutions"
MLN_DATABASE = f"{DATA_DIR}/mln_db.mln"
DOMAIN_P_DECS = f'{DATA_DIR}/mln_grid_p_decs.txt'
GridWorldGenerator.generate_data(output_dir=PROBLEM_STATE_DSET_DIR)
FFXSolver.solve_problem_dir(
    domain_file=DOMAIN_FILE,
    problem_dir=PROBLEM_STATE_DSET_DIR,
    output_dir=PROBLEM_SOLUTION_DIR,
)

write_dbs(
    domain_file=DOMAIN_FILE,
    problem_state_dir=PROBLEM_STATE_DSET_DIR,
    problem_solution_dir=PROBLEM_SOLUTION_DIR,
    mln_db_path=MLN_DATABASE,
)
MLNDeclarationGenerator.gen(DOMAIN_FILE, DOMAIN_P_DECS)
model = PracmlnLearningModel(mln_database_path=MLN_DATABASE, domain_p_decs_path=DOMAIN_P_DECS)
model.train()