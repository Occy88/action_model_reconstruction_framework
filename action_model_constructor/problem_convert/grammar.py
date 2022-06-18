class LarkGrammar:
    @staticmethod
    def str_literal(item: str):
        """
        lark reads arg as string
        :param item:
        :return:
        """
        return f'"{item}"'

    @staticmethod
    def one_or_more(item: str):
        return f"{item}+"

    @staticmethod
    def zero_or_more(item: str):
        return f"{item}*"

    @staticmethod
    def zero_or_one(item: str):
        return f"{item}?"

    @staticmethod
    def exactly_n(item: str, n: int):
        return f"{item} ~ {n}"

    @staticmethod
    def between_n_m(item: str, n: int, m: int):
        return f"{item} ~{n}..{m}"

    @staticmethod
    def match_one_of(items: list):
        return " | ".join(items)
