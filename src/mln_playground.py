from pddl_parser.pddl_22_parser.pddl_parser import parse_pddl

from generator.state_to_json import parse_state
from problem_convert.plan_trace_gen import Predicate
from problem_convert.plan_trace_gen import State
from solvers.ffx.plan_to_json import parse_plan


# //modify precondition to  pre(a,b, past)
#   modify negation to neg(a,b, current)


def add_q(ls):
    return list(map(lambda x: "?" + x, ls))


def add_pre(pred, preconditions):
    pre = ""
    for p in preconditions:
        a = p["args"]
        pre += "^" + p["name"] + "(" + ",".join(a) + ",0)"
    return "(" + pred + pre + ")"


def write_action(name, args, predicate, preconditions):
    score = "\n0.000000    "
    action_sig = name + "(" + ",".join(args) + ")"

    return (
        score
        + action_sig
        + " => "
        + add_pre(
            predicate["name"] + "(" + ", ".join(list(predicate["args"])) + ",1)",
            preconditions,
        )
    )


def write_neg_action(name, args, predicate, preconditions):
    score = "\n0.000000    "
    action_sig = name + "(" + ",".join(args) + ")"

    return (
        score
        + action_sig
        + " => "
        + add_pre(
            predicate["name"] + "(" + ", ".join(list(predicate["args"])) + ",-1)",
            preconditions,
        )
    )


def write_state(f, s, p):
    f.write("\n" + p.mln(cap_args=True))
    f.write(s.mln(cap_args=True, extra_args=["0"]))


def write_db(f, state, plan):
    # f.write(state.mln(cap_args=True))
    for index, s in enumerate(plan["steps"]):
        p = Predicate(**s["predicate"])
        write_state(f, state, p)
        state.perform_action(p)

        for pr in state.latest_removed:
            f.write("\n" + pr.mln(cap_args=True, extra_args=["-1"]))
        for pr in state.latest_added:
            f.write("\n" + pr.mln(cap_args=True, extra_args=["1"]))

        if index < len(plan["steps"]) - 1:
            f.write("\n--- ")


domain = "grid"
parsed = parse_pddl("../domains/" + domain + ".pddl")

# # state.perform_action('move-b-to-t', ('b9', 'b4'))
# mln_params = 'mln_params.mln'
mln_database = "mln_db.mln"
# f = open(mln_params, 'w')
#
#
# f.write("// predicate declarations")
# f.write("\nt = {-1,0,1}")
# for a in parsed['actions']:
#     f.write('\n' + a['name'] + '(' + ','.join(['object'] * len(a['args'])) + ')')
#
# for p in parsed['predicates']:
#     f.write('\n' + p['name'] + '(' + ','.join(['object'] * len(p['args'])) + ',t)')
# f.write("\n\n// formulas: ")
#
# for a in parsed['actions']:
#     score = '\n0.000000    '
#     action_sig = a['name'] + '(' + ','.join(a['args']) + ')'
#     pre_p = '^'.join(list(map(lambda x: Predicate(**x).mln(extra_args=['1']), a['effect']['positive'])))
#     pre_n = '^'.join(list(map(lambda x: Predicate(**x).mln(extra_args=['-1']), a['effect']['negative'])))
#     precon = '^'.join(list(map(lambda x: Predicate(**x).mln(extra_args=['0']), a['precondition'])))
#     f.write(score + action_sig + ' ^ ' + precon + ' => ' + pre_p + ' ^ ' + pre_n)
#     # f.write("\n\n// positives: ")
#     # for p in a['effect']['positive']:
#     #     f.write(write_action(a['name'], a['args'], p, a['precondition']))
#     # # f.write("\n\n// negatives: ")
#     # for p in a['effect']['negative']:
#     #     f.write(write_neg_action(a['name'], a['args'], p, a['precondition']))
# f.close()


fl = open(mln_database, "w")

# f.write('\n\n//databae test \n\n')
for i in range(1, 100):
    try:
        state = State(parsed)
        problem = parse_state(domain, "state_" + str(i))
        state.set_init_state(problem["init"])
        plan = parse_plan(domain, "state_" + str(i))
        print(len(plan["steps"]))
        write_db(fl, state, plan)
        fl.write("\n---\n")
    except FileNotFoundError:
        continue
fl.close()
