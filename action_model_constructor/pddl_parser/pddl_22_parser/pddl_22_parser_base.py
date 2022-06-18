from abc import ABC
from abc import abstractmethod


class BasePDDL22Domain(ABC):
    """
    Base class for PDDL 2.2 Domain file parser.

    <domain> ::= (define (domain <name>)
                    [<extension-def>]
                    [<require-def>]
                    [<types-def>]:typing
                    [<constants-def>]
                    [<domain-vars-def>]:expressionevaluation
                    [<predicates-def>]
                    [<timeless-def>]
                    [<safety-def>]:safetyconstraints
                    <structure-def>
                    )
    <extension-def> ::= (:extends <domain name>+)
    <require-def> ::= (:requirements <require-key>+)
    <require-key> ::= See Section 15
    <types-def> ::= (:types <typed list (name)>)
    <constants-def> ::= (:constants <typed list (name)>)
    <domain-vars-def> ::= (:domain-variables
    <typed list(domain-var-declaration)>)
    <predicates-def> ::= (:predicates <atomic formula skeleton>+)
        <atomic formula skeleton>
            ::= (<predicate> <typed list (variable)>)
                <predicate> ::= <name>
                <variable> ::= ?<name>
                <timeless-def> ::= (:timeless <literal (name)>+)
    <structure-def> ::= <action-def>
    <structure-def> ::=:domainaxioms <axiom-def>
    <structure-def> ::=:actionexpansions <method-def>
    """

    @abstractmethod
    def define(self, *args):
        """
        Start of pddl domain file
        signature: (define
                        <domain>
                        <extends>
                        <requirements>
                        <types>
                        <constants>
                        <domain-variables>
                        <predicates>
                        <timeless>
                        <action>
                        <axiom>
                        <method>
        :param args:
        :return:
        """
        pass

    @abstractmethod
    def domain(self, *args, **kwargs):
        """
        pddl domain name
        signature: (domain str)
        :param args:
        :param kwargs:
        :return:
        """
        pass

    @abstractmethod
    def extends(self, *args, **kwargs):
        """
        pddl domain extends
        signature: (:extends str+)

        :extends argument is present, then this domain inherits requirements, types,
        constants, actions, axioms, and timelessly true propositions from the named domains, which
        are called the ancestors of this domain.

        :param args:
        :param kwargs:
        :return:
        """
        pass

    @abstractmethod
    def requirements(self, *args, **kwargs):
        """
        pddl domain requirements
        signature: (:requirments :str+ )
        :param args:
        :param kwargs:
        :return:
        """
        pass

    @abstractmethod
    def types(self, *args, **kwargs):
        """
        pddl domain types
        signature: (:types <typed list (name)>+)
        :param args:
        :param kwargs:
        :return:
        """
        pass

    @abstractmethod
    def constants(self, *args, **kwargs):
        """
        pddl domain constants
        signature: (:constants <typed list (name)>+)
        :param args:
        :param kwargs:
        :return:
        """
        pass

    @abstractmethod
    def domain_variables(self, *args, **kwargs):
        """
        pddl domain variables
        signature: (:domain-variables <typed list (domain-var-declaration)>+)
        :param args:
        :param kwargs:
        :return:
        """
        pass

    @abstractmethod
    def predicates(self, *args, **kwargs):
        """
        pddl predicates
        signature: (:predicates <predicate_format>+)
                    > predicate_format: (name <typed_variable>+)
                    > typed_variable: ?name - ?type
        :param args:
        :param kwargs:
        :return:
        """
        pass

    @abstractmethod
    def timeless(self, *args, **kwargs):
        """
        signature: (:timeless <name>+)
        :param args:
        :param kwargs:
        :return:
        """
        pass

    @abstractmethod
    def action(self, *args, **kwargs):
        """
        signature: (:action name <action_structure>)
        :param args:
        :param kwargs:
        :return:
        """
        pass

    @abstractmethod
    def axiom(self, *args, **kwargs):
        """
        signature: (:axiom <axiom_structure)
        :param args:
        :param kwargs:
        :return:
        """
        pass

    @abstractmethod
    def method(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        pass
