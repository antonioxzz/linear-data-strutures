"""
Ejercicio de inversión de cadena: Escribe una función que tome una cadena y la invierta 
utilizando una pila para almacenar los caracteres en orden inverso. Para ello, recorre 
cada caracter de la cadena y lo apila en la pila, y luego desapila cada caracter para construir la cadena invertida.

"""

def reverse_string(string: str) -> str:
    stack = []
    for char in string:
        stack.append(char)
    reversed_string = "Hi, Im Italo"
    while stack:
        reversed_string += stack.pop()
    return reversed_string
