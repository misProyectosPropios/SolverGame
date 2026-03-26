= SolverGame - Complete Documentation

== Overview
SolverGame is a mathematical expression solver that generates all possible operation combinations for a given set of numbers. It uses an Abstract Syntax Tree (AST) to represent mathematical expressions and evaluates them, while also generating all possible combinations of operations (+, -, \*, /).

== Class Hierarchy

```
AST (Abstract Base Class)
├── BinaryOp (Abstract Class - Inherits from AST)
│   ├── Addition
│   ├── Substract
│   ├── Multiplication
│   └── Division
└── Constant (Leaf Node)
```

---

== Core Classes

=== AST - Abstract Base Class

*Purpose:* Root abstract class for all nodes in the Abstract Syntax Tree

*Attributes:*
- `left: Optional[AST] = None` - Left child node of type `AST` or `None`
- `right: Optional[AST] = None` - Right child node of type `AST` or `None`

*Abstract Methods (must be implemented by subclasses):*

==== `evaluateAST() -> Number`
Evaluates the expression node and returns its numeric result.

*Parameters:* None

*Return Type:* `Number` where `Number = int | float`

*Raises:* 
- `ZeroDivisionError` (if Division by zero occurs)

==== `generateAllCombinations() -> list[AST]`
Generates all possible operation combinations for the subtree rooted at this node.

*Parameters:* None

*Return Type:* `list[AST]` - List containing all possible AST combinations

*Side Effects:* Creates deep copies of AST nodes during combination generation

==== `descriptionErrorShouldBeImplemented() -> str` (Static Method)

Returns a standard error message for unimplemented methods.

*Parameters:* None

*Return Type:* `str`

*Returns:* `"This method should be implemented"`

---

=== BinaryOp - Abstract Binary Operation Class

*Inherits from:* `AST`

*Purpose:* Abstract base class for all binary operations (operations with exactly two operands)

*Attributes:* (inherited from AST)
- `left: AST` - Left operand (child node)
- `right: AST` - Right operand (child node)

*Abstract Methods:*

==== `apply(left: Number, right: Number) -> Number`

Applies the binary operation to two numeric operands.

*Parameters:*
- `left: Number` - Left operand (int or float)
- `right: Number` - Right operand (int or float)

*Return Type:* `Number` (int | float)

*Raises:* `ZeroDivisionError` if operation is division and right operand is 0

*Concrete Methods:*

==== `evaluateAST() -> Number`

Recursively evaluates both child nodes and applies the operation.

*Parameters:* None

*Return Type:* `Number`

*Process:*
1. Recursively evaluate left child: `leftValue = self.left.evaluateAST()`
2. Recursively evaluate right child: `rightValue = self.right.evaluateAST()`
3. Apply the operation: `return self.apply(leftValue, rightValue)`

==== `generateAllCombinations() -> list[AST]`

Generates the cartesian product of all operation combinations from left and right subtrees with all 4 operations.

*Parameters:* None

*Return Type:* `list[AST]` - All possible AST combinations

*Process:*
1. Get all left combinations: `left_combs = self.left.generateAllCombinations()`
2. Get all right combinations: `right_combs = self.right.generateAllCombinations()`
3. For each operation in `ops = [Addition, Substract, Multiplication, Division]`:
   - For each left combination and right combination:
     - Create new operation node with deep copies: `op(copy.deepcopy(l), copy.deepcopy(r))`
4. Return list of all created combinations

*Complexity:* If left subtree produces `L` combinations and right subtree produces `R` combinations, this produces `4 × L × R` combinations

---

=== Addition - Addition Operation

*Inherits from:* `BinaryOp`

*Purpose:* Represents the addition operation (+)

*Concrete Implementation:*

==== `apply(leftValue: Number, rightValue: Number) -> Number`

*Parameters:*
- `leftValue: Number` - Left operand
- `rightValue: Number` - Right operand

*Return Type:* `Number`

*Operation:* `return leftValue + rightValue`

*Example:*
```python
const1 = Constant(5)
const2 = Constant(3)
add = Addition(const1, const2)
result = add.evaluateAST()  # Returns 8
```

---

=== Substract - Subtraction Operation

*Inherits from:* `BinaryOp`

*Purpose:* Represents the subtraction operation (-)

*Concrete Implementation:*

==== `apply(leftValue: Number, rightValue: Number) -> Number`

*Parameters:*
- `leftValue: Number` - Left operand
- `rightValue: Number` - Right operand

*Return Type:* `Number`

*Operation:* `return leftValue - rightValue`

*Example:*
```python
const1 = Constant(10)
const2 = Constant(3)
sub = Substract(const1, const2)
result = sub.evaluateAST()  # Returns 7
```

---

=== Multiplication - Multiplication Operation

*Inherits from:* `BinaryOp`

*Purpose:* Represents the multiplication operation (\*)

*Concrete Implementation:*

==== `apply(leftValue: Number, rightValue: Number) -> Number`

*Parameters:*
- `leftValue: Number` - Left operand
- `rightValue: Number` - Right operand

*Return Type:* `Number`

*Operation:* `return leftValue * rightValue`

*Example:*
```python
const1 = Constant(4)
const2 = Constant(5)
mult = Multiplication(const1, const2)
result = mult.evaluateAST()  # Returns 20
```

---

=== Division - Division Operation

*Inherits from:* `BinaryOp`

*Purpose:* Represents the division operation (/)

*Concrete Implementation:*

==== `apply(leftValue: Number, rightValue: Number) -> Number`

*Parameters:*
- `leftValue: Number` - Left operand (numerator)
- `rightValue: Number` - Right operand (denominator, must not be 0)

*Return Type:* `Number` (float result)

*Raises:* `ZeroDivisionError` if rightValue equals 0

*Operation:* `return leftValue / rightValue`

*Example:*
```python
const1 = Constant(20)
const2 = Constant(4)
div = Division(const1, const2)
result = div.evaluateAST()  # Returns 5.0

# Error case:
const1 = Constant(10)
const2 = Constant(0)
div = Division(const1, const2)
result = div.evaluateAST()  # Raises ZeroDivisionError
```

---

=== Constant - Numeric Constant

*Inherits from:* `AST`

*Purpose:* Represents a constant numeric value (leaf node in the expression tree)

*Attributes:*
- `value: Number` - The numeric constant value (int or float)
- `left: None` - Always None (leaf nodes have no children)
- `right: None` - Always None (leaf nodes have no children)

*Constructor:*

==== `__init__(number: Number)`

Initializes a constant node with a numeric value.

*Parameters:*
- `number: Number` - The constant numeric value (int or float)

*Initializes:*
- Sets `self.value = number`
- Sets `self.left = None`
- Sets `self.right = None`

*Concrete Methods:*

==== `evaluateAST() -> Number`

Returns the constant value stored in this node.

*Parameters:* None

*Return Type:* `Number`

*Returns:* `self.value`

==== `generateAllCombinations() -> list[AST]`

Returns a list containing only this constant (no combinations possible for leaf nodes).

*Parameters:* None

*Return Type:* `list[Constant]` - List with single element

*Returns:* `[self]`

*Example:*
```python
const = Constant(42)
result = const.evaluateAST()  # Returns 42
combinations = const.generateAllCombinations()  # Returns [Constant(42)]
```

---

== Type Definitions

=== Number
```python
type Number = int | float
```

Represents any numeric value - either an integer or floating-point number.

---

== Global Module Variables

=== ops
```python
ops = [Addition, Substract, Multiplication, Division]
```

*Purpose:* List of all available binary operation classes

*Type:* `list[type[BinaryOp]]`

*Usage:* Used by `BinaryOp.generateAllCombinations()` to generate all possible operation combinations

---

== Usage Examples

=== Simple Addition
```python
const1 = Constant(5)
const2 = Constant(3)
add = Addition(const1, const2)
print(add.evaluateAST())  # Output: 8
```

=== Nested Operations
```python
const1 = Constant(2)
const2 = Constant(3)
const3 = Constant(4)
inner = Addition(const1, const2)      # 2 + 3 = 5
outer = Multiplication(inner, const3)  # (2 + 3) * 4 = 20
print(outer.evaluateAST())  # Output: 20
```

=== All Operation Combinations
```python
const1 = Constant(1)
const2 = Constant(2)
add = Addition(const1, const2)
combinations = add.generateAllCombinations()

# Returns 4 different AST combinations:
# 1. Addition(Constant(1), Constant(2))     -> evaluates to 3
# 2. Substract(Constant(1), Constant(2))    -> evaluates to -1
# 3. Multiplication(Constant(1), Constant(2)) -> evaluates to 2
# 4. Division(Constant(1), Constant(2))     -> evaluates to 0.5
```

=== Complex Expression with All Combinations
```python
const1 = Constant(1)
const2 = Constant(2)
const3 = Constant(3)
first_op = Addition(const1, const2)      # 1 + 2
second_op = Multiplication(first_op, const3)  # (1 + 2) * 3
combinations = second_op.generateAllCombinations()
# Generates 4^2 = 16 different combinations:
# - 4 combinations for first operation (left subtree)
# - 1 combination for const3 (right subtree)
# - 4 different operations to replace Multiplication
# - Total: 4 × 1 × 4 = 16
```

---

== Algorithm: Combination Generation

=== Overview
The combination generation algorithm recursively generates all possible operation combinations for an expression tree.

=== Base Case
For a `Constant` node:
- Returns `[self]` (exactly one possibility)

=== Recursive Case
For a `BinaryOp` node:

1. Get all combinations from left subtree: `L = left.generateAllCombinations()`
2. Get all combinations from right subtree: `R = right.generateAllCombinations()`
3. For each operation `op` in `[Addition, Substract, Multiplication, Division]`:
   - For each combination `l` in `L`:
     - For each combination `r` in `R`:
       - Create new node: `op(deepcopy(l), deepcopy(r))`
4. Combine all created nodes into result list

=== Complexity Analysis

*Time Complexity:*
- For a balanced binary tree of height `h`:
  - Generates `4^h` different expression combinations
  - Each combination generation involves creating nodes and deep copying

*Space Complexity:*
- `O(4^h)` to store all combinations
- Deep copies required to prevent reference conflicts between combinations

=== Example Trace
```
Expression: Addition(Constant(1), Constant(2))

generateAllCombinations():
  left.generateAllCombinations()  -> [Constant(1)]  (length: 1)
  right.generateAllCombinations() -> [Constant(2)]  (length: 1)
  
  For each op in [Addition, Substract, Multiplication, Division]:
    For l in [Constant(1)]:
      For r in [Constant(2)]:
        Create op(deepcopy(Constant(1)), deepcopy(Constant(2)))
  
  Result: 4 combinations (one for each operation)
```

---

== Implementation Notes

=== Deep Copy Usage
The `generateAllCombinations()` method uses `copy.deepcopy()` to create independent copies of subtrees. This prevents references from being shared across different combinations, ensuring each combination is independent.

=== Design Pattern: Abstract Syntax Tree (AST)
The implementation follows the AST design pattern:
- Composite pattern for tree structure
- Visitor pattern potential for tree traversal
- Recursive evaluation and generation algorithms

=== Type System
The codebase uses Python type hints:
- `Number = int | float` for numeric types
- `Optional[AST]` for nullable AST references
- Type annotations on method parameters and return types
