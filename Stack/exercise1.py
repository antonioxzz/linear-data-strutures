"""
Ejercicio de verificación de paréntesis: Escribe una función que tome una cadena que contiene paréntesis, 
corchetes y llaves, y verifique si los paréntesis están balanceados. Es decir, que cada paréntesis abierto 
tenga su correspondiente paréntesis cerrado en el orden correcto. Utiliza una pila para llevar un seguimiento 
de los paréntesis abiertos y cierra el último paréntesis abierto si se encuentra un paréntesis cerrado.

"""

def balanced_parentheses(string: str) -> bool:
    stack = []
    opening = "([{"
    closing = ")]}"
    for char in string:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return False
            last_open = stack.pop()
            if opening.index(last_open) != closing.index(char):
                return False
    return not stack