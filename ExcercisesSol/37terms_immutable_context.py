# to be able to specify type annotations and static type checker mypy
from typing import Dict
# importation of abc module for abstract base classes
from abc import ABCMeta, abstractmethod
# for enum support
from enum import Enum, auto

"""
This grammar defines term that can be evaluated using a context to bind values to variables

          Term ::= Constant
                 | Variable
                 | Expression
    Expression ::= Term BinaryOp Term
                 | UnaryOp Term 
"""


class EmptyException(Exception):
    """Empty string exception, raised whenever an empty string is not expected"""

    def __init__(self, message):
        self.message = message


class NotBoundException(Exception):
    """Variable without binding exception, raised whenever a variable is not bound with a value"""

    def __init__(self, message):
        self.message = message


class Context:
    """
    Stores the values assigned to the variables into a lookup table (a dictionary).
    Each entry of the lookup table is a pair (name of variable, value)
    Some methods allows us to bind a value to a named variable,
    to change the assignment and to evaluate a variable.
    This version is almost immutable.
    """
    def __init__(self, lookup_table) -> None:
        self.lookup_table = lookup_table
        
    def bind(self, name: str, value: float):
        if not name:  # is name empty
            raise EmptyException("The variable's name is empty in bind()")
        # creates a new Context add the assignment (name, value) and returns it
        # the following is equivalent to
        # self.lookup_table[name] = value
        # return(Context(self.lookup_table)
        # which performs explicitly a assignment
        # this notation is available from Python 3.5 see PEP 448
        return Context({ **self.lookup_table, name:value})

    def get_value(self, name: str) -> float:
        if not name:  # name is empty
            raise EmptyException("The variable's name is empty in get_value()")
        if name in self.lookup_table:
            return self.lookup_table[name]
        else:
            raise NotBoundException("The variable '" + name + "' is not bound to a value")


class BinOp(Enum):
    """Enumeration of all supported binary operators"""
    ADD = auto()
    SUB = auto()
    MUL = auto()
    DIV = auto()


class UnaOp(Enum):
    """Enumeration of all supported unary operators"""
    NEG = auto()


class Term(metaclass=ABCMeta):
    """
    This abstract class defines a abstract method that evaluates
    a term (expression)
    """
    @abstractmethod
    def eval(self, context: Context) -> float:
        """
        Abstract method that evaluate a term.
        :param context: where the bindings (variable name, value) are stored
        :return: the value of the evaluated term
        """
        pass               # no implementation


class Constant(Term):
    """
    The value of a constant cannot (obviously) change.
    The value is initialized during the creation.
    """
    def __init__(self, value: float) -> None:
        """
        Defines the constant value.
        :param value: the constant value to initialize
        """
        self.value = value

    def eval(self, context: Context) -> float:
        """
        :return: simply the value
        """
        return self.value


class Variable(Term):
    """
    The value of a variable can be modified via the context object.
    """
    def __init__(self, name: str) -> None:
        """
        A variable is created and added to the context
        :param name: name of the variable
        :raises EmptyException: when the variable's name is empty
        """
        if not name:  # is name is empty
            raise EmptyException("The variable's name cannot be empty in Variable")
        self.name = name

    def eval(self, context: Context) -> float:
        """
        :return: the value of the variable
        """
        return context.get_value(self.name)


class BinaryExpression(Term):
    """
    A binary expression has two terms (left, right) and a binary operator.
    """
    def __init__(self, left: Term, right: Term, bin_op: BinOp) -> None:
        """
        :param left: left term
        :param right: right term
        :param bin_op: binary operator (enum)
        """
        self.left = left
        self.right = right
        self.bin_op = bin_op

    def eval(self, context: Context) -> float:
        """
        Evaluates both the terms first and then apply the binary_operator
        :return: the evaluated value of the binary expression
        :raises ZeroDivisionError for division operator
        """
        value_left = self.left.eval(context)
        value_right = self.right.eval(context)
        bin_op_dict = {BinOp.ADD: lambda l, r: l + r,
                       BinOp.SUB: lambda l, r: l - r,
                       BinOp.MUL: lambda l, r: l * r,
                       BinOp.DIV: lambda l, r: l / r
                       }

        operation = bin_op_dict[self.bin_op]
        return operation(value_left, value_right)


class UnaryExpression(Term):
    """
    A unary expression has on term and a unary operator.
    """
    def __init__(self, term: Term, una_op: UnaOp) -> None:
        """
        :param term: single term
        :param una_op: binary operator (enum)
        """
        self.term = term
        self.una_op = una_op

    def eval(self, context: Context) -> float:
        """
        Evaluates both the terms first and then apply the binary_operator
        :return: the evaluated value of the binary expression
        """
        value_term = self.term.eval(context)
        una_op_dict = {UnaOp.NEG: lambda t: (-1) * t}
        operation = una_op_dict[self.una_op]
        return operation(value_term)


def main() -> None:
    """ Launcher """
    ctx = Context({})
    three = Constant(3)
    five = Constant(5)
    zero = Constant(0)
    print("Constant 3: ", three.eval(ctx))
    print("Constant 5: ", five.eval(ctx))
    print("Constant 0: ", zero.eval(ctx))
    v = Variable("d")
    ctx = ctx.bind("d", 7)      # define d = 7

    try:
        print("Variable d: ", v.eval(ctx))
    except EmptyException as empty:
        print(empty.message)
    except NotBoundException as not_bound:
        print(not_bound.message)

    neg = UnaryExpression(v, UnaOp.NEG)
    print("-d: ", neg.eval(ctx))
    addition = BinaryExpression(three, neg, BinOp.ADD)
    print("3 + (-d): ", addition.eval(ctx))
    multiplication = BinaryExpression(addition, five, BinOp.MUL)
    print("(3 + -d) * 5: ", multiplication.eval(ctx))

    try:
        v2 = Variable("v2")
        print("Variable v2: ", v2.eval(ctx))
    except (EmptyException, NotBoundException) as error:
        print(error.message)

    try:
        v3 = Variable("")
        print("Variable v3: ", v3.eval(ctx))
    except (EmptyException, NotBoundException) as error:
        print(error.message)

    try:
        ctx = ctx.bind("", 55)
    except (EmptyException, NotBoundException) as error:
        print(error.message)

    div_by_zero = BinaryExpression(three, zero, BinOp.DIV)
    try:
        print(div_by_zero.eval(ctx))
    except ZeroDivisionError:
        print("Division by zero is not possible")

    # for the following statement the ZeroDivisionError exception is not caught
    # the exception will be finally detected at the very top level and an
    # error message will be displayed by the Python interpreter.
    # uncomment the following line.
    # print(div_by_zero.eval(ctx))


if __name__ == "__main__":
    main()
