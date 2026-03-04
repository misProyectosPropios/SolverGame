= Documentation

==
To generate all possible expression we are going to do a biyection with the naturals.

=== Enumeration Order
1. AST height
2. Total node count
3. Operator arity (unary < binary)
4. Operator symbol order
5. Left subtree index, then right subtree index

== DSA

- Use AST to model the way the operations are handled

== Functions

=== evaluateAST(ast: AST) -> Number | $bot$

=== generateExpression(numberList: List[Number], numberExpression) ->