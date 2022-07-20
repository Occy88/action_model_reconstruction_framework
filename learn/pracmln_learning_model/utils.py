from pddl_parser.pddl_22_parser.pddl_parser import parse_pddl

from generator.state_to_json import parse_state
from learn.pracmln_learning_model.state_inference import Predicate
from learn.pracmln_learning_model.state_inference import State
from solvers.ffx.plan_to_json import parse_plan



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


def write_dbs(
    domain_file: str,
    problem_state_dir: str,
    problem_solution_dir: str,
    mln_db_path: str,
):
    parsed = parse_pddl(domain_file)
    fl = open(mln_db_path, "w+")
    a = 1
    for i in range(1, 100):
        try:
            state = State(parsed)
            problem = parse_state(f"{problem_state_dir}/state_{i}")
            state.set_init_state(problem["init"])
            plan = parse_plan(f"{problem_solution_dir}/state_{i}")
            print(len(plan["steps"]))
            write_db(fl, state, plan)
            fl.write("\n---\n")
            a += 1
        except Exception as e:
            print(e)
            continue
    fl.close()
    print(a)

def load_dbs(path:str):
    databases = open(path).read()
    databases = databases.strip("\n").strip(" ").strip("---").split("---")
    return databases

class MLNDeclarationGenerator:

    @classmethod
    def gen(cls, domain_file_path: str, out_path: str):
        parsed = parse_pddl(domain_file_path)
        f = open(out_path, 'w')
        f.write("// predicate declarations")
        f.write("\nt = {-1,0,1}")
        for a in parsed['actions']:
            num_actions = len(a['args'])

            f.write('\n' + a['name'] + '(' + ','.join(['object'] * num_actions) + ')')

        for p in parsed['predicates']:
            num_preds = len(p['args'])
            f.write(f'\n {p["name"]} ({",".join(["object"] * num_preds)}')
            if num_preds == 0:
                f.write('t)')
            else:
                f.write(',t)')
        # f.write("\n\n// formulas: ")

        # for a in parsed['actions']:
        #     score = '\n0.000000    '
        #     action_sig = a['name'] + '(' + ','.join(a['args']) + ')'
        #     pre_p = '^'.join(list(map(lambda x: Predicate(**x).mln(extra_args=['1']), a['effect']['positive'])))
        #     pre_n = '^'.join(list(map(lambda x: Predicate(**x).mln(extra_args=['-1']), a['effect']['negative'])))
        #     precon = '^'.join(list(map(lambda x: Predicate(**x).mln(extra_args=['0']), a['precondition'])))
        #     f.write(score + action_sig + ' ^ ' + precon + ' => ' + pre_p + ' ^ ' + pre_n)

        f.close()
