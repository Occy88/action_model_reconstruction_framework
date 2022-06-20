from lark import Transformer


class Predicate(Transformer):
    @staticmethod
    def predicate(args):
        val = args[0].children[0]
        return val
