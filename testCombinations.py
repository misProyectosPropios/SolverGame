import unittest
from decider import * 
from solver import *

class TestStringMethods(unittest.TestCase):

    def test_constant(self):
        const: Constant = Constant(1)
        res: set = const.generateAllCombinations()
        self.assertEqual(len(res), 1)

    def test_addition_combinations(self):
        const1: Constant = Constant(1)
        const2: Constant = Constant(2)
        add: Addition = Addition(const1, const2)
        res: set = add.generateAllCombinations()

        self.assertEqual(len(res), 4)
        addition_ast = Addition(Constant(1), Constant(2))
        multiplication_ast = Multiplication(Constant(1), Constant(2))
        substract_ast = Substract(Constant(1), Constant(2))
        division_ast = Division(Constant(1), Constant(2))
        self.assertIn(addition_ast, res)
        self.assertIn(multiplication_ast, res)
        self.assertIn(substract_ast, res)
        self.assertIn(division_ast, res)

    def test_multiplication_combinations(self):
        const1: Constant = Constant(1)
        const2: Constant = Constant(2)
        multiplication: Addition = Multiplication(const1, const2)
        res: set = multiplication.generateAllCombinations()

        self.assertEqual(len(res), 4)
        addition_ast = Addition(Constant(1), Constant(2))
        multiplication_ast = Multiplication(Constant(1), Constant(2))
        substract_ast = Substract(Constant(1), Constant(2))
        division_ast = Division(Constant(1), Constant(2))
        self.assertIn(addition_ast, res)
        self.assertIn(multiplication_ast, res)
        self.assertIn(substract_ast, res)
        self.assertIn(division_ast, res)

    def test_substract_combinations(self):
        const1: Constant = Constant(1)
        const2: Constant = Constant(2)
        substract: Addition = Substract(const1, const2)
        res: set = substract.generateAllCombinations()

        self.assertEqual(len(res), 4)
        addition_ast = Addition(Constant(1), Constant(2))
        multiplication_ast = Multiplication(Constant(1), Constant(2))
        substract_ast = Substract(Constant(1), Constant(2))
        division_ast = Division(Constant(1), Constant(2))
        self.assertIn(addition_ast, res)
        self.assertIn(multiplication_ast, res)
        self.assertIn(substract_ast, res)
        self.assertIn(division_ast, res)

    def test_division_combinations(self):
        const1: Constant = Constant(1)
        const2: Constant = Constant(2)
        division: Addition = Division(const1, const2)
        res: set = division.generateAllCombinations()

        self.assertEqual(len(res), 4)
        addition_ast = Addition(Constant(1), Constant(2))
        multiplication_ast = Multiplication(Constant(1), Constant(2))
        substract_ast = Substract(Constant(1), Constant(2))
        division_ast = Division(Constant(1), Constant(2))
        self.assertIn(addition_ast, res)
        self.assertIn(multiplication_ast, res)
        self.assertIn(substract_ast, res)
        self.assertIn(division_ast, res)

    def test_multiple_operations(self):
        const1: Constant = Constant(1)
        const2: Constant = Constant(2)
        const3: Constant = Constant(3)
        add: Addition = Division(const1, const2)
        division: Multiplication = Multiplication(add, const3)
        res: set = division.generateAllCombinations()

        self.assertEqual(len(res), 4 ** 2)


if __name__ == '__main__':
    unittest.main()