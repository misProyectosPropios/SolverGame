import unittest
from decider import * 


class TestCombinationsMethods(unittest.TestCase):

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

class TestShapesMethod(unittest.TestCase):
    def test_noConstant(self):
        res: list[AST] = generateAllGraphs([])
        self.assertEqual(len(res), 0)

    def test_oneConstant(self):
        res: list[AST] = generateAllGraphs([Constant(1)])
        self.assertEqual(len(res), 1)

    def test_twoConstant(self):
        res: list[AST] = generateAllGraphs([Constant(1), Constant(2)])
        self.assertEqual(len(res), 4)

    def test_threeConstant(self):
        lista_const = [Constant(1), Constant(2), Constant(3)]
        res: list[AST] = generateAllGraphs(lista_const)
        self.assertEqual(len(res), 32)

class TestParenthesisNeeded(unittest.TestCase):
    def test_constant(self):
        value: AST = Constant(2)
        res: int = value.numberOfParenthesisNeeded()
        self.assertEqual(res, 0)

    def test_addition(self):
        value: AST = Addition(Constant(2), Constant(3))
        res: int = value.numberOfParenthesisNeeded()
        self.assertEqual(res, 0)

    def test_multiplication(self):
        value: AST = Multiplication(Constant(2), Constant(3))
        res: int = value.numberOfParenthesisNeeded()
        self.assertEqual(res, 0)

    def test_MultipleAddition(self):
        value: AST = Addition(Constant(2), Addition(Constant(3), Constant(5)))
        res: int = value.numberOfParenthesisNeeded()
        self.assertEqual(res, 0)

    def test_MultipleMultiplication(self):
        value: AST = Multiplication(Constant(2), Multiplication(Constant(3), Constant(5)))
        res: int = value.numberOfParenthesisNeeded()
        self.assertEqual(res, 0)

    def test_multiplicationOfAddition(self):
        value: AST = Multiplication(Constant(2), Addition(Constant(3), Constant(5)))
        res: int = value.numberOfParenthesisNeeded()
        self.assertEqual(res, 1)

    def test_multiplicationBetweenTwoAdditions(self):
        value: AST = Multiplication(Addition(Constant(1), Constant(3)), Addition(Constant(0), Constant(5)))
        res: int = value.numberOfParenthesisNeeded()
        self.assertEqual(res, 2)

class TestParenthesisNeeded(unittest.TestCase):
    def test_prettifyInConstant(self):
        value: AST = Constant(2)
        res: str  = value.prettifyMinParenthesis()
        self.assertEqual(res, "2")

    def test_prettifyAddition(self):
        value: AST = Addition(Constant(2), Constant(4))
        res: str  = value.prettifyMinParenthesis()
        self.assertEqual(res, "2+4")

    def test_prettifyMultiplication(self):
        value: AST = Multiplication(Constant(2), Constant(4))
        res: str  = value.prettifyMinParenthesis()
        self.assertEqual(res, "2*4")

    def test_prettifyMultiplicationOfAddition(self):
        value: AST = Multiplication(Constant(2), Addition(Constant(3), Constant(4)))
        res: str  = value.prettifyMinParenthesis()
        self.assertEqual(res, "2*(3+4)")

if __name__ == '__main__':
    unittest.main()