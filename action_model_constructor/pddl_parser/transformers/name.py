from lark import Transformer


class Name(Transformer):
    @staticmethod
    def name(args):
        val = args[0].value
        return val
