from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional
import copy

type Number = int | float



@dataclass
class AST(ABC):
    # These are the class-level type hints you were looking for
    left: Optional['AST'] = None
    right: Optional['AST'] = None

    @abstractmethod
    def evaluateAST(self):
        """This method must be implemented by all subclasses."""
        pass

    @abstractmethod
    def generateAllCombinations(self):
        """This method must be implemented by all subclasses."""
        pass

    @staticmethod
    def descriptionErrorShouldBeImplemented():
        return "This method should be implemented"

class BinaryOp(AST):
    @abstractmethod
    def apply(self, left: Number, right: Number) -> Number:
        raise self.descriptionErrorShouldBeImplemented

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

class Addition(BinaryOp):
    def apply(self, leftValue, rightValue) -> Number:
        return leftValue + rightValue
    
class Substract(BinaryOp):
    def apply(self, leftValue, rightValue):
        return leftValue - rightValue

class Multiplication(BinaryOp):
    def apply(self, leftValue, rightValue):
        return leftValue * rightValue

class Division(BinaryOp):
    def apply(self, leftValue, rightValue):
        return leftValue / rightValue

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
    
    def generateAllCombinations(self):
        return [self]