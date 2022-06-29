from generator.state_to_json import parse_state
from solvers.ffx.plan_to_json import parse_plan

from domain.simulator import Predicate, State
from pddl_parser.pddl_22_parser.pddl_parser import parse_pddl


# //modify precondition to  pre(a,b, past)
#   modify negation to neg(a,b, current)

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

    # @classmethod
    # def _add_q(cls, l):
    #     return list(map(lambda x: "?" + x, l))
    #
    # @classmethod
    # def _add_pre(cls, pred, preconditions):
    #     pre = ""
    #     for p in preconditions:
    #         a = p["args"]
    #         pre += "^" + p["name"] + "(" + ",".join(a) + ",0)"
    #     return "(" + pred + pre + ")"
    #
    # @classmethod
    # def _write_action(cls, name, args, predicate, preconditions):
    #     score = "\n0.000000    "
    #     action_sig = name + "(" + ",".join(args) + ")"
    #
    #     return (
    #             score
    #             + action_sig
    #             + " => "
    #             + cls._add_pre(
    #         predicate["name"] + "(" + ", ".join(list(predicate["args"])) + ",1)",
    #         preconditions,
    #     )
    #     )
    #
    # @classmethod
    # def _write_neg_action(cls, name, args, predicate, preconditions):
    #     score = "\n0.000000    "
    #     action_sig = name + "(" + ",".join(args) + ")"
    #
    #     return (
    #             score
    #             + action_sig
    #             + " => "
    #             + cls._add_pre(
    #         predicate["name"] + "(" + ", ".join(list(predicate["args"])) + ",-1)",
    #         preconditions, )
    #     )

    # f.write("\n\n// positives: ")
    # for p in a['effect']['positive']:
    #     f.write(write_action(a['name'], a['args'], p, a['precondition']))
    # # f.write("\n\n// negatives: ")
    # for p in a['effect']['negative']:
    #     f.write(write_neg_action(a['name'], a['args'], p, a['precondition']))
