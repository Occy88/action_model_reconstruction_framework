import os
from unittest import TestCase
from lark import Lark
from pddl_parser.transformers import Name


class TestGrammarName(TestCase):
    def setUp(self) -> None:
        self.grammar = """
        start:name
        %import .name.name
        %import common (WS)
        %ignore WS
        """
        self.transformer = Name()
        self.import_path = [f'{os.getcwd()}/../../grammar/']
        self.parser = "lalr"

    def test_name_parses_kebab_case(self):
        try:
            parser = Lark(grammar=self.grammar, import_paths=self.import_path, parser=self.parser)
            parser.parse("""name-with-dashes""")
        except Exception as e:
            self.fail(msg=e)

    def test_name_parses_snake_case(self):
        try:
            parser = Lark(grammar=self.grammar, import_paths=self.import_path, parser=self.parser)
            parser.parse("""name_with_underscores""")
        except Exception as e:
            self.fail(msg=e)

    def test_name_parsing_fails(self):
        parser = Lark(grammar=self.grammar, import_paths=self.import_path, parser=self.parser)
        self.assertRaises(Exception, parser.parse, """space separated""", msg='failed to raise on space separator')
        self.assertRaises(Exception, parser.parse, """(not-char""", msg='failed to raise on non char in word')
        self.assertRaises(Exception, parser.parse, """1not-num""", msg='failed to raise on num in word')

    def test_name_transformer(self):
        try:
            parser = Lark(grammar=self.grammar, import_paths=self.import_path, transformer=self.transformer,
                          parser=self.parser)
            parser.parse("""name-with-dashes""")
        except Exception as e:
            self.fail(msg=e)
