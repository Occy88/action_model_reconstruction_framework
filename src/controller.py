import os

from generator.generator import Generator
from parser.ff_to_action import FFToActionParser
from solvers.solvers import FFXSolver

base_path = os.path.normpath(f'{os.getcwd()}/..')
# generator
grid_desk = "-x 5 -y 5 -t 15 -k 20 -l 20 -p 100"
pddl = "grid"
g = Generator()
g.gen_problem_states(pddl, 100, grid_desk)
s = FFXSolver()
s.solve_problem_dir(f'{base_path}/domains/{pddl}.pddl', f'{base_path}/generator/{pddl}/states',
                    f'{base_path}/solvers/plans/{pddl}')

p = FFToActionParser()
p.parse_all(pddl)
