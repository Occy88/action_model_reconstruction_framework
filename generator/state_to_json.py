from lark import Lark, Transformer, v_args

import os


class PddlToJson(Transformer):
    def problem(self, args):
        definition = args[0]
        domain = args[1]
        objects = args[2]
        init = args[3]
        goal = args[4]
        return {
            "definition": definition,
            "domain": domain,
            "objects": objects,
            "init": init[0],
            "goal": goal[0],
        }

    def var(self, v):
        val = v[0]
        return val

    def parameters(self, args):
        return list(args)

    def definition(self, name):
        return name

    def domain(self, name):
        return name

    def predicate(self, args):
        name = args[0]
        vals = list(tuple(args[1:]))
        p = {"name": name, "args": vals}
        return p

    init = list

    predicates = list
    objects = list
    goal = list

    def string(self, s):
        s = s[0].value
        return s.replace("-", "_")

    number = v_args(inline=True)(float)


def parse_state(state_f_path):
    sample_domain = open(state_f_path, "r").read()
    grammar = open(f'{os.path.dirname(__file__)}/grammar', "r").read()
    parser = Lark(grammar, transformer=PddlToJson(), parser="lalr")
    parsed = parser.parse(sample_domain)
    return parsed
