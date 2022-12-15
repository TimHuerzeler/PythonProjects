"""
Collection of unit tests for term_exceptions.py
"""

import unittest
from term_exceptions import *

class Test_context(unittest.TestCase):

    def test_bind_get_value(self):
        """Checks that binding an identifier with a value and get_value return the same value"""
        identifier = "v"
        value = 10.5
        a_var = Variable(identifier)
        ctx = Context()
        ctx.bind(identifier, value)
        self.assertEqual(ctx.get_value(identifier), value)

    def test_bind_empty(self):
        """Checks that binding an empty identifier raises an exception"""
        identifier = ""
        ctx = Context()
        value = 0.0
        with self.assertRaises(EmptyException):
            ctx.bind(identifier, value)

    def test_get_value_empty(self):
        """Checks that getting a value for an empty identifier raises an exception"""
        identifier = ""
        ctx = Context()
        with self.assertRaises(EmptyException):
            ctx.get_value(identifier)


class Test_constant(unittest.TestCase):

    def test_eval(self):
        """Checks the evaluation of a constant works fine"""
        value = 4.03
        four = Constant(value)
        ctx  = Context()
        self.assertEqual(Constant.eval(four, ctx), value)


class Test_variable(unittest.TestCase):

    def test_eval(self):
        """Checks that the evaluation of a variable works fine"""
        identifier = "v"
        value = 10.5
        a_var = Variable(identifier)
        ctx = Context()
        ctx.bind(identifier, value)
        self.assertEqual(a_var.eval(ctx), value)

    def test_creation_empty(self):
        """Checks that the creation of an empty variable raises an exception"""
        emtpy_identifier = ""
        with self.assertRaises(EmptyException):
            a_var = Variable(emtpy_identifier)


class Test_binary_expression(unittest.TestCase):

    def test_eval(self):
        """Checks that the evaluation of a binary expression works fine for each operator"""
        value = 5.0
        term = Constant(value)
        ctx = Context()
        bin_expr = Binary_expression(term, term, Bin_op.ADD)
        self.assertEqual(bin_expr.eval(ctx), value+value)
        bin_expr = Binary_expression(term, term, Bin_op.SUB)
        self.assertEqual(bin_expr.eval(ctx), value-value)
        bin_expr = Binary_expression(term, term, Bin_op.MUL)
        self.assertEqual(bin_expr.eval(ctx), value*value)
        value2 = 2.0
        term_right = Constant(value2)
        bin_expr = Binary_expression(term, term_right, Bin_op.DIV)
        self.assertEqual(bin_expr.eval(ctx), value/value2)

    def test_division_by_zero(self):
        ctx = Context()
        five = Constant(5.0)
        zero = Constant(0.0)
        bin_expr_division_by_zero = Binary_expression(five, zero, Bin_op.DIV)
        with self.assertRaises(ZeroDivisionError):
            bin_expr_division_by_zero.eval(ctx)


class Test_unary_expression(unittest.TestCase):

    def test_eval(self):
        """Checks that the evaluation of a unary expression works fine"""
        value = 5.0
        term = Constant(value)
        ctx = Context()
        una_expr = Unary_expression(term, Una_op.NEG)
        self.assertEqual(una_expr.eval(ctx), (-1) * value)

if __name__ == '__main__':
    unittest.main()