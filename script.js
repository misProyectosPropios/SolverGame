let pyodide;

python_code = `
from abc import ABC, abstractmethod
from dataclasses import dataclass
import itertools
from typing import Optional
import copy

type Number = int | float



@dataclass
class AST(ABC):
    # These are the class-level type hints you were looking for
    left: Optional['AST'] = None
    right: Optional['AST'] = None

    def __str__(self) -> str:
        return self.prettifyMinParenthesis()

    @abstractmethod
    def evaluateAST(self):
        """This method must be implemented by all subclasses."""
        pass

    @abstractmethod
    def generateAllCombinations(self):
        """This method must be implemented by all subclasses."""
        pass

    @abstractmethod
    def prettify(self):
        """Prints the arithmetic expression in infix notation with all parenthesis"""
        pass
        
    @abstractmethod
    def prettifyMinParenthesis(self):
        """Prints the arithmetic expression in infix notation with only the needed parenthesis"""
        pass

    @abstractmethod
    def numberOfParenthesisNeeded(self, parent_prec: int = 0) -> int:
        """Return the minimum number of parenthesis to the expression"""
        pass

    def hasAtMostOneParenthesis(self) -> bool:
        return self.numberOfParenthesisNeeded() <= 1

    @staticmethod
    def descriptionErrorShouldBeImplemented():
        return "This method should be implemented"

    

class BinaryOp(AST):
    @abstractmethod
    def apply(self, left: Number, right: Number) -> Number:
        pass

    @abstractmethod
    def symbol(self) -> str:
        raise self.descriptionErrorShouldBeImplemented

    def prettify(self):
        return f"({self.left.prettify()} {self.symbol()} {self.right.prettify()})"

    def prettifyMinParenthesis(self, parent_prec: int = 0):
        prec = self.precedence()
        if prec < parent_prec:
                return f"({self.prettifyMinParenthesis(prec)})"
        return f"{self.left.prettifyMinParenthesis(prec)}{self.symbol()}{self.right.prettifyMinParenthesis(prec)}"

    def evaluateAST(self) -> Number:
        leftValue = self.left.evaluateAST()
        rightValue = self.right.evaluateAST()
        return self.apply(leftValue, rightValue)

    def generateAllCombinations(self):
        left_combs = self.left.generateAllCombinations()
        right_combs = self.right.generateAllCombinations()

        return [
            op(copy.deepcopy(l), copy.deepcopy(r))
            for op in ops
            for l in left_combs
            for r in right_combs
        ]
    
    def numberOfParenthesisNeeded(self, parent_prec: int = 0) -> int:
        """Return the minimum number of parenthesis to the expression"""
        count: int = 0
        if parent_prec > self.precedence():
            count += 1
        count += self.left.numberOfParenthesisNeeded(self.precedence())
        count += self.right.numberOfParenthesisNeeded(self.precedence())

        return count 



class Addition(BinaryOp):
    def apply(self, leftValue, rightValue) -> Number:
        return leftValue + rightValue

    def symbol(self) -> str:
        return "+"

    def precedence(self) -> int:
        return 1

class Substract(BinaryOp):
    def apply(self, leftValue, rightValue):
        return leftValue - rightValue

    def symbol(self) -> str:
        return "-"

    def precedence(self) -> int:
        return 1

class Multiplication(BinaryOp):
    def apply(self, leftValue, rightValue):
        return leftValue * rightValue

    def symbol(self) -> str:
        return "*"
    
    def precedence(self) -> int:
        return 2

class Division(BinaryOp):
    def apply(self, leftValue, rightValue):
        return leftValue / rightValue

    def symbol(self) -> str:
        return "/"
    
    def precedence(self) -> int:
        return 2


ops = [Addition, Substract, Multiplication, Division]

@dataclass
class Constant(AST):
    value: Number = 0

    def __init__(self, number: Number):
        self.left = None
        self.right = None
        self.value = number

    def evaluateAST(self):
        return self.value
    
    def prettify(self):
        return str(self.value)

    def prettifyMinParenthesis(self, parent_prec: int = 0):
        """Prints the arithmetic expression in infix notation with only the needed parenthesis"""
        return str(self.value)

    def generateAllCombinations(self):
        return [self]

    def numberOfParenthesisNeeded(self, parent_prec: int = 0) -> int:
        """Return the minimum number of parenthesis to the expression"""
        return 0

def generateAllGraphs(constants: list[Constant]) -> list[AST]:
    """
    Generates all possible expression trees using the given constants in the provided order.
    """
    if not constants:
        return []

    def build_shapes(nodes: list[AST]) -> list[AST]:
        if len(nodes) == 1:
            return [nodes[0]]
        
        shapes = []
        for i in range(1, len(nodes)):
            left_shapes = build_shapes(nodes[:i])
            right_shapes = build_shapes(nodes[i:])
            for l in left_shapes:
                for r in right_shapes:
                    # Addition is used as a placeholder for the tree structure.
                    shapes.append(Addition(l, r))
        return shapes

    # 1. Generate all possible tree structures (shapes)
    all_shapes = build_shapes(constants)
    
    # 2. For each shape, expand into all operator combinations (+, -, *, /)
    all_graphs = []
    for shape in all_shapes:
        all_graphs.extend(shape.generateAllCombinations())
    
    return all_graphs

def isThereOptionThatGeneratesNumberX(options: list[AST], value: int) -> list[AST]:
    res = []
    allValues = []
    for index, option in enumerate(options):
        evaluate: Number
        try:
            evaluate = option.evaluateAST()
            allValues.append((index, evaluate))
        except ZeroDivisionError:
            continue
        hasParenthesisAtMostRequired = option.hasAtMostOneParenthesis()
        if evaluate == value and hasParenthesisAtMostRequired:
            res.append(option)
    return res

def isThereOptionThatGeneratesNumberXInAllPermutations(options: list[AST], value: int) -> list[AST]:    
    allOptions = []
    perms = itertools.permutations(options)
    for perm in perms:
        res = isThereOptionThatGeneratesNumberX(generateAllGraphs(list(perm)), value)
        allOptions += res
    return allOptions

def obtainSolution(values: list[int], value: int) -> list[AST]:
    return isThereOptionThatGeneratesNumberXInAllPermutations(values, value)


def main():
    list_res = obtainSolution([Constant(1), Constant(1), Constant(5), Constant(1)], 10)
    for res in list_res:
        print(res)
`

async function init() {
    pyodide = await loadPyodide();
    // 🔥 Load Python file from repo
    const response = await fetch("main.py");
    const code = await response.text();

    // 🔥 Write into Pyodide filesystem
    pyodide.FS.writeFile("main.py", code);

    await pyodide.runPythonAsync(`
import sys
if "" not in sys.path:
    sys.path.append("")
    `);

    //await pyodide.runPythonAsync(python_code);

    document.getElementById("solveBtn").disabled = false;
    return pyodide;
}

let pyodideReadyPromise = init();
async function run() {
    
    let pyodide = await pyodideReadyPromise;

    const numbers = document.getElementById("numbers").value;
    const target = document.getElementById("target").value;
        
    const result = await pyodide.runPythonAsync(`
import importlib
import main
importlib.reload(main)

nums = [main.Constant(int(x)) for x in "${numbers}".split(",")]
res = main.obtainSolution(nums, int(${target}))

[f"{str(r)} = {r.evaluateAST()}" for r in res[:20]]
    `);
    
    document.getElementById("output").textContent = result;

}

init();
