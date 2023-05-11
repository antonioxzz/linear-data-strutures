"""
Escribe un programa que lea un archivo de texto y cuente la cantidad de veces que aparece cada palabra en el archivo. 
Luego, almacena los resultados en un diccionario y muestra los pares palabra-frecuencia en orden alfabético.

"""

import string


def count_words(my_file) -> dict:
    frequency = {}
    with open(my_file, 'r') as file:
        for line in file:
            line = line.translate(str.maketrans('', '', string.punctuation)).lower()
            for word in line.split():
                if word in frequency:
                    frequency[word] += 1
                else:
                    frequency[word] = 1

    return dict(sorted(frequency.items()))

frequency = count_words('Ejercicios ioet/Dic/my_file.txt')
for word, frequency in frequency.items():
    print(word, frequency)