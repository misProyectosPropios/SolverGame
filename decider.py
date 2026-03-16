from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

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

    @staticmethod
    def descriptionErrorShouldBeImplemented():
        return "This method should be implemented"

class Addition(AST):
    def evaluateAST(self) -> Number:
        leftValue: Number = self.left.evaluateAST()
        rightValue: Number = self.right.evaluateAST()
        return leftValue + rightValue
    
class Substract(AST):
    def evaluateAST(self):
        leftValue: Number = self.left.evaluateAST()
        rightValue: Number = self.right.evaluateAST()
        return leftValue - rightValue

class Multiplication(AST):
    def evaluateAST(self):
        leftValue: Number = self.left.evaluateAST()
        rightValue: Number = self.right.evaluateAST()
        return leftValue * rightValue

class Division(AST):
    def evaluateAST(self):
        leftValue: Number = self.left.evaluateAST()
        rightValue: Number = self.right.evaluateAST()
        return leftValue / rightValue

@dataclass
class Constant(AST):
    value: Number = 0

    def __init__(self, number: Number):
        self.left = None
        self.right = None
        self.value = number

    def evaluateAST(self):
        return self.value