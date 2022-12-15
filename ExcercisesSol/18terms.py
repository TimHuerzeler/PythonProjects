"""
Definition of terms according the following grammar and
implement an eval() method that evaluates them.

Term ::= Constant
       | Variable
       | Expression
Expression ::= Term BinaryOp Term
             | UnaryOp Term
"""

# to be able to use exit() that abort the program
import sys
# to be able to specify type annotations
from typing import Dict
# importation of abc module for abstract base classes
from abc import ABC, abstractmethod


class Context:
    """
    Stores the values assigned to the variables into a lookup table (a dictionary).
    Each entry of the lookup table is a pair (name of variable , value)
    Some methods allows us to bind a value to a named variable,
    to change the assigment and to evaluate a variable.
    """
    def __init__(self) -> None:
        self.lookup_table: Dict[str, float] = {}

    def get_value(self, name: str) -> float:
        if not name:
            print("The variable's name is empty")
            sys.exit()

        if name in self.lookup_table:
            return self.lookup_table[name]
        else:
            print("The variable '" + name + "' is not bound to a value")
            sys.exit()

    def bind(self, name: str, value: float) -> None:
        """
        If the variable, called name, does not exists in the dictionary 
        lookup_table then a new assigment is added into the dictionary otherwise
        the value of the variable is changed.
        :param name: name of the variable
        :param value: value to assign to the variable
        """
        if not name:  # is name empty
            print("The variable's name is empty")
            sys.exit()
        self.lookup_table[name] = value


class Term(metaclass=ABC):
    """
    This abstract class defines an abstract method that evaluates a term (expression)
    """
    @abstractmethod
    def eval(self, context: Context) -> float:
        pass  # abstract method do not have any implementation


class Constant(Term):
    """
    The value of a constant cannot (obviously) change.
    The value is initialized during the creation.
    """
    def __init__(self, value: float) -> None:
        self.value = value

    def eval(self, context: Context) -> float:
        return self.value


class Variable(Term):
    """
    The value of a variable can be modified via the context object.
    """
    def __init__(self, name: str) -> None:
        self.name = name

    def eval(self, context: Context) -> float:
        return context.get_value(self.name)

   
class BinaryExpression(Term):
    """
    A binary expression is composed of two terms (left, right) and a binary operator.
    """
    def __init__(self, left: Term, right: Term, bin_op: str) -> None:
        self.left = left
        self.right = right
        self.bin_op = bin_op

    def eval(self, context: Context) -> None:
        value_left = self.left.eval(context)
        value_right = self.right.eval(context)
        bin_op_dict = {  # other binary operators can be easily added
            "+": lambda l, r: l + r,
            "-": lambda l, r: l - r,
            "*": lambda l, r: l * r,
            "/": lambda l, r: l / r
            }
        operation = bin_op_dict[self.bin_op]
        return operation(value_left, value_right)


class UnaryExpression(Term):
    """
    A unary expression is composed of a single term and a unary operator.
    """
    def __init__(self, term: Term, una_op: str) -> None:
        self.term = term
        self.una_op = una_op

    def eval(self, context: Context) -> None:
        value_term = self.term.eval(context)
        una_op_dict = {  # other unary operators can be easily added
            "-": lambda t: (-1.0) * t
        }
        operation = una_op_dict[self.una_op]
        return operation(value_term)


def main() -> None:
    """
    Launcher
    Sample program that illustrate the creation of following term
       ((3 + (-d)) * 5)   where the variable d is 7
    and its evaluation by means of the eval() method.
    """
    ctx = Context()
    three = Constant(3)
    five = Constant(5)
    print("Constant 3: ", three.eval(ctx))
    print("Constant 5: ", five.eval(ctx))
    v = Variable("d")
    ctx.bind("d", 7)      # define d = 7
    print("Variable d: ", v.eval(ctx))
    neg = UnaryExpression(v, "-")
    print("-d: ", neg.eval(ctx))
    addition = BinaryExpression(three, neg, "+")
    print("3 + -d: ", addition.eval(ctx))
    multiplication = BinaryExpression(addition, five, "*")
    print("(3 + -d) * 5: ", multiplication.eval(ctx))


if __name__ == "__main__":
    main()
