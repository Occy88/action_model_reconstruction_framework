# from collections import namedtuple
#
# from lark import Lark, Transformer
#
# from problem_convert.grammar import LarkGrammar as lg
#
# name = namedtuple("name", "x")
#
#
# class Name:
#     """
#     Names of domains, like other occurrences of syntactic category <name>,
#     are strings of characters beginning with a letter and containing letters,
#     digits, hyphens (\-"),and underscores (\ ").
#     Case is not significant.
#     """
#
#     key = "name"
#
#     def name(self, args):
#         return name(*args)
#
#     def lark_grammar(self):
#         name_regex = "/([a-zA-Z]|\d)+((_|-)([a-zA-Z]|\d)+)*/"
#         grammar = [self.key, ":", name_regex]
#         return " ".join(grammar)
#
#
# variable = namedtuple("variable", "x")
#
#
# class Variable:
#     """
#     <variable> ::= ?<name>
#
#     """
#
#     key = "variable"
#
#     def variable(self, args):
#         variable(*args)
#
#     def lark_grammar(self):
#         grammar = [self.key, ":", lg.str_literal("?"), Name.key]
#         return " ".join(grammar)
#
#
# either = namedtuple("either", "x")
# fluent = namedtuple("fluent", "x")
# ptype = namedtuple("ptype", "x")
#
#
# class Type:
#     """
#     <type> ::= <name>
#     <type> ::= (either <type>+)
#     <type> ::=:fluents (fluent <type>)
#     """
#
#     key = "type"
#
#     def type(self, args):
#         return ptype(args)
#
#     def type_1(self, args):
#         return args
#
#     def type_2(self, args):
#         return either(args)
#
#     def type_3(self, args):
#         return fluent(args)
#
#     def lark_grammar(self):
#         f_1 = [f"{self.key}_1", ":", Name.key]
#         f_2 = [
#             f"{self.key}_2",
#             ":",
#             lg.str_literal("("),
#             lg.str_literal("either"),
#             lg.one_or_more(self.key),
#             lg.str_literal(")"),
#         ]
#         f_3 = [
#             f"{self.key}_3",
#             ":",
#             lg.str_literal("("),
#             lg.str_literal("fluent"),
#             self.key,
#             lg.str_literal(")"),
#         ]
#         f_0 = [self.key, ":", lg.match_one_of([f_1[0], f_2[0], f_3[0]])]
#         asstr = [" ".join(x) for x in [f_1, f_2, f_3, f_0]]
#         return "\n".join(asstr)
#
#
# class TypedList:
#     """
#     <typed list (x)> ::= x
#     <typed list (x)> ::=:typing x+ - <type> <typed list(x)>
#     """
#
#     def __init__(self, x: str):
#         self.x = x
#         self.key = f"typed_list_{x}"
#
#     def lark_grammar(self) -> (dict, str):
#         """
#         {self.key}_{x} : tl_1_{x} | tl_2_{x}
#         {self.key}_1_{x}       : x
#         {self.key}_2_{x}       : x+ "-" type typed_list_{x}
#
#         :param x:
#         :return: name:str, grammar:str
#         """
#         f_1 = [f"{self.key}_1", ":", self.x]
#         f_2 = [
#             f"{self.key}_2",
#             ":",
#             lg.one_or_more(self.x),
#             lg.str_literal("-"),
#             Type.key,
#             self.key,
#         ]
#         f_0 = [f"{self.key}:", lg.match_one_of([f_1[0], f_2[0]])]
#         asstr = [" ".join(x) for x in [f_1, f_2, f_0]]
#         return "\n".join(asstr)
#
#
# typed_list_variable = namedtuple("typed_list_variable", "x")
#
#
# class TypedListVariable(TypedList, Transformer):
#     def __init__(self):
#         super().__init__(Variable.key)
#
#     def typed_list_variable(self, args):
#         return typed_list_variable(args)
#
#
# # def test_parse():
# #     grammar = TypedList.lark_grammar()
# #     print(grammar)
# #     parser = Lark(grammar, transformer=TypedList(), parser="lalr")
# #     sample = """or or not octavio"""
# #     out = parser.parse(sample)
# #
# #     print(out)
#
#
# # test_parse()
