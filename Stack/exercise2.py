"""
Ejercicio de evaluación de expresiones posfijas: Escribe una función que tome una expresión posfija 
(notación polaca inversa) y calcule su resultado utilizando una pila para almacenar los operandos. 
Para evaluar la expresión, recorre cada elemento de la cadena y si es un operando lo apila en la pila, 
si es un operador lo desapila junto con los dos operandos previos y aplica la operación correspondiente, 
y apila el resultado de vuelta en la pila.

"""

def evaluate_postfix_expression(expression: str) -> float:
    stack = []
    operators = set("+-*/")
    for token in expression.split():
        if token not in operators:
            stack.append(float(token))
        else:
            right_operand = stack.pop()
            left_operand = stack.pop()
            if token == "+":
                result = left_operand + right_operand
            elif token == "-":
                result = left_operand - right_operand
            elif token == "*":
                result = left_operand * right_operand
            elif token == "/":
                result = left_operand / right_operand
            stack.append(result)
    return stack.pop()
