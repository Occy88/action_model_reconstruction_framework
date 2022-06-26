from pddl_parser.pddl_22_parser.pddl_parser import parse_pddl

from generator.state_to_json import parse_state
from learn.pracmln_learning_model.state_inference import Predicate
from learn.pracmln_learning_model.state_inference import State
from solvers.ffx.plan_to_json import parse_plan


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
