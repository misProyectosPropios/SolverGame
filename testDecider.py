import unittest
from decider import * 

class TestStringMethods(unittest.TestCase):

    def test_constant(self):
        const: Constant = Constant(1)
        self.assertEqual(const.evaluateAST(), 1)
        self.assertNotEqual(const.evaluateAST(), 0)

    def test_sum(self):
        const1: Constant = Constant(1)
        const2: Constant = Constant(2)
        sum: Addition = Addition(const1, const2)
        self.assertEqual(sum.evaluateAST(), 1 + 2)
        self.assertNotEqual(sum.evaluateAST(), 1)

    def test_multiplication(self):
        const1: Constant = Constant(2)
        const2: Constant = Constant(5)
        mult: Multiplication = Multiplication(const1, const2)
        self.assertEqual(mult.evaluateAST(), 5 * 2)
        self.assertNotEqual(mult.evaluateAST(), 1)

    def test_substract(self):
        const1: Constant = Constant(10)
        const2: Constant = Constant(5)
        substract: Substract = Substract(const1, const2)
        self.assertEqual(substract.evaluateAST(), 10 - 5)
        self.assertNotEqual(substract.evaluateAST(), 10)

    def test_division_without_zero(self):
        const1: Constant = Constant(10)
        const2: Constant = Constant(5)
        division: Division = Division(const1, const2)
        self.assertEqual(division.evaluateAST(), 10 / 5)
        self.assertNotEqual(division.evaluateAST(), 1)

    def test_division_over_zero(self):
        const1: Constant = Constant(10)
        const2: Constant = Constant(0)
        division: Division = Division(const1, const2)
        self.assertRaises(ZeroDivisionError, division.evaluateAST())
if __name__ == '__main__':
    unittest.main()