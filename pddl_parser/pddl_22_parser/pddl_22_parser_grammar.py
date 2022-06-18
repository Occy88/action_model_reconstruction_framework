from pddl_22_parser_base import BasePDDL22Domain
from ..grammar import LarkGrammar as lg


class PDDL22DomainGrammar(BasePDDL22Domain):

    def get_grammar(self):
        grammar = [
            '?start: define',
            self.define()
            self.domain(),
            self.extends(),
            self.requirements(),
            self.types(),
            self.requirements(),
            self.constants(),
            self.domain_variables(),
            self.timeless(),
            self.action(),
            self.method(),
            self.variable(),
            self.typed_name(),
            self.typed_var(),
            self.colon_name(),
            self.tuple_name(),
            self.name()
        ]
        return '\n'.join(grammar)

    def define(self, *args):
        grammar = [
            'define:',
            lg.str_literal('('),
            self.domain.__name__,
            lg.zero_or_one(self.extends.__name__),
            lg.zero_or_one(self.requirements.__name__),
            lg.zero_or_one(self.types.__name__),
            lg.zero_or_one(self.constants.__name__),
            lg.zero_or_one(self.domain_variables.__name__),
            self.predicates.__name__,
            lg.zero_or_one(self.timeless.__name__),
            lg.one_or_more(self.action.__name__),
            lg.zero_or_more(self.axiom.__name__),
            self.method.__name__,
            lg.str_literal(')'),
        ]
        return ' '.join(grammar)

    def domain(self, *args, **kwargs):
        grammar = [
            'domain:',
            lg.str_literal('define'),
            lg.str_literal('('),
            lg.str_literal('domain'),
            self.name.__name__,
            lg.str_literal(')')
        ]
        return ' '.join(grammar)

    def extends(self, *args, **kwargs):
        grammar = [
            'extends:',
            lg.str_literal('('),
            lg.str_literal(':extends'),
            lg.one_or_more(self.name.__name__),
            lg.str_literal(')')
        ]
        return ' '.join(grammar)

    def requirements(self, *args, **kwargs):
        grammar = [
            'requirements:',
            lg.str_literal('('),
            lg.str_literal(':requirements'),
            lg.one_or_more(self.colon_name.__name__)

        ]
        return ' '.join(grammar)

    def types(self, *args, **kwargs):
        grammar = [
            'types:',
            lg.str_literal('('),
            lg.str_literal(':types'),
            lg.one_or_more(self.typed_name.__name__),
            lg.str_literal(')')
        ]
        return ' '.join(grammar)

    def constants(self, *args, **kwargs):
        grammar = [
            'constants:',
            lg.str_literal('('),
            lg.str_literal(':constants'),
            lg.one_or_more(self.typed_name.__name__),
            lg.str_literal(')')
        ]
        return ' '.join(grammar)

    def domain_variables(self, *args, **kwargs):
        """
        deprecated.
        :param args:
        :param kwargs:
        :return:
        """
        grammar = [

        ]
        return ' '.join(grammar)

    def predicates(self, *args, **kwargs):
        grammar = [
        ]
        return ' '.join(grammar)

    def timeless(self, *args, **kwargs):
        grammar = [
            'timeless:',
            lg.str_literal('('),
            lg.str_literal(':timeless'),
            lg.one_or_more(self.tuple_name.__name__),
            lg.str_literal(')')
        ]
        return ' '.join(grammar)

    def action(self, *args, **kwargs):
        """
        <action-def> ::= (:action <action functor>
            :parameters ( <typed list (variable)> )
        <action-def body>)
        <action functor> ::= <name>
        <action-def body> ::= [:vars (<typed list(variable)>)]
                                            :existential-preconditions
                                            :conditional-effects
                            [:precondition <GD>]
                            [:expansion
                            <action spec>]:actionexpansions
                            [:expansion :methods]:actionexpansions
                            [:maintain <GD>]:actionexpansions
                            [ :effect <effect>]
                            [:only-in-expansions <boolean>]:actionexpans
        :param args:
        :param kwargs:
        :return:
        """
        grammar = [
            'action:',
            lg.str_literal('('),
            lg.str_literal(':action'),
            self.name.__name__,
            lg.str_literal(':parameters'),
            self.conditional_statement.__name__
            lg.str_literal(':precondition'),
            self.goal_descriptor.__name__,
            lg.str_literal(':effect'),

            lg.str_literal(')')
        ]
        return ' '.join(grammar)

    def axiom(self, *args, **kwargs):
        grammar = [
        ]
        return ' '.join(grammar)

    def method(self, *args, **kwargs):
        grammar = [
        ]
        return ' '.join(grammar)

    def typed_name(self):
        grammar = [
            'typed_name:',
            lg.one_or_more(self.name.__name__),
            lg.str_literal('-'),
            self.name.__name__,
        ]
        return ' '.join(grammar)

    def typed_var(self):
        grammar = [
            'typed_var:',
            lg.one_or_more(self.var.__name__),
            lg.str_literal('-'),
            self.name.__name__,
        ]
        return ' '.join(grammar)

    def colon_name(self):
        """
        pddl colon prepended string
        :return:
        """
        grammar = [
            'colon_name:',
            lg.str_literal(':'),
            self.name.__name__
        ]
        return ' '.join(grammar)

    def tuple_name(self):
        grammar = [
            'tuple_name:',
            lg.str_literal('('),
            lg.exactly_n(self.name.__name__, 2),
            lg.str_literal(')')
        ]
        return ' '.join(grammar)

    def axiom(self):
        """
        <axiom-def> ::= (:axiom
                            :vars (<typed list (variable)>)
                            :context <GD>
                            :implies <literal(term)>)
        :return:
        """
        pass

    def goal_descriptor(self):
        """
        <GD> ::= <atomic formula(term)>
        <GD> ::= (and <GD>)
        <GD> ::= <literal(term)>
        <GD> ::=:disjunctivepreconditions (or <GD>)
        <GD> ::=:disjunctivepreconditions (not <GD>)
        <GD> ::=:disjunctivepreconditions (imply <GD> <GD>)
        <GD> ::=:existentialpreconditions
                (exists (<typed list(variable)>) <GD> )
        <GD> ::=:universalpreconditions
                (forall (<typed list(variable)>) <GD>)
        :return:
        """

    def literal(self, t: str):
        """
        > )
        <literal(t)> ::= <atomic formula(t)>
        <literal(t)> ::= (not <atomic formula(t) >)
        :return:
        """
        literal_1 = [
            self.atomic_formula(t)[0],
        ]
        literal_2 = [
            lg.str_literal('('),
            lg.str_literal('not'),
            lg.str_literal()
        ]

    def atomic_formula(self, t: str) -> (str, str):
        """
        <atomic formula(t)> ::= (<predicate> t*)
        :return:
        """
        name = f'{self.atomic_formula.__name__}_{str(hash(t))}'
        grammar = [
            f'{name}:',
            lg.str_literal('('),
            self.predicate.__name__,
            lg.zero_or_more(t),
            lg.str_literal(')')
        ]
        return name, ' '.join(grammar)

    def term(self):
        """

        <term> ::= <name>
        <term> ::= <variable>
        :return:
        """
        term_1 = [
            self.name.__name__,
        ]
        term_2 = [
            self.variable.__name__,
        ]
        grammar = [
            'term:',
            lg.match_one_of([term_1, term_2])
        ]
        return ' '.join(grammar)

    def predicate(self):
        """
        <predicate> ::= <name>
        :return:
        """
        grammar = [
            'predicate:',
            self.name.__name__,
        ]
        return ' '.join(grammar)

    def variable(self):
        """
        <variable> ::= ?<name>
        :return:
        """
        grammar = [
            'variable:',
            lg.str_literal('?'),
            self.name.__name__
        ]
        return ' '.join(grammar)

    def typed_list(self, x: str) -> (str, str):
        """
        Ensure that when using this function,
        instance with relevant type is initiated in root

        <typed list (x)> ::= x
        <typed list (x)> ::=:typing x+ - <type> <typed list(x)>
        :param x:
        :return: name:str, grammar:str
        """
        name = f'{self.typed_list.__name__}_{str(hash(x))}'
        tl_1 = [
            x
        ]
        tl_2 = [
            lg.one_or_more(x),
            lg.str_literal('-'),
            self.type.__name__,
            name,
        ]
        grammar = [
            f'{name}:',
            lg.match_one_of([tl_1, tl_2])
        ]
        return name, ' '.join(grammar)

    def type(self):
        """
        <type> ::= <name>
        <type> ::= (either <type>+)
        <type> ::=:fluents (fluent <type>)
        :return:
        """
        type_1 = [
            self.name.__name__
        ]
        type_2 = [
            lg.str_literal('('),
            lg.str_literal('either'),
            lg.one_or_more(self.type.__name__),
            lg.str_literal(')')
        ]
        type_3 = [
            lg.str_literal('('),
            lg.str_literal('fluent'),
            self.type.__name__,
            lg.str_literal(')')
        ]
        all_types = list(' '.join(x) for x in [type_1, type_2, type_3])
        grammar = [
            'type :',
            lg.match_one_of(all_types)
        ]
        return ' '.join(grammar)

    @staticmethod
    def name():
        """
        Names of domains, like other occurrences of syntactic category <name>,
        are strings of characters beginning with a letter and containing letters,
        digits, hyphens (\-"),and underscores (\ ").
        Case is not signicant.
        :return:
        """
        name_regex = '/([a-zA-Z]|\d)+((_|-)([a-zA-Z]|\d)+)*/'
        grammar = [
            'name :',
            name_regex
        ]
        return ' '.join(grammar)

    @staticmethod
    def p_or():
        return 'p_or: "or"'

    @staticmethod
    def p_and():
        return 'p_and: "and"'

    @staticmethod
    def p_not():
        return 'p_not: "not"'

    @staticmethod
    def p_exists():
        return 'p_exists: "exists"'

    @staticmethod
    def p_forall():
        return 'p_forall: "forall"'

    @staticmethod
    def p_change():
        return 'p_change: "change"'

    @staticmethod
    def p_when():
        return 'p_when: "when"'

    @staticmethod
    def p_choice():
        return 'p_choice: "choice"'

    @staticmethod
    def p_forsome():
        return 'p_forsome: "forsome"'

class LARKGrammar:
    def __init__(self, name, ):
class NOT:
    def