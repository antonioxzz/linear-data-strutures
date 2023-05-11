"""
Ejercicio de registro de notas: Escribe un programa que permita registrar las notas de varios estudiantes y 
luego calcule el promedio de notas de cada estudiante y el promedio general de la clase utilizando un diccionario para almacenar los datos.

"""

def average(scores: float) -> float:
    return sum(scores)/len(scores)

students: dict[str, list[float]] = {}

num_students = int(input("Enter the number of scores to register: "))

for i in range(num_students):
    name: str = input("Enter the student's name: ")
    scores_input: str = input("Enter student grades separated by commas: ")
    scores: list[float]= [float(score.strip()) for score in scores_input.split(",")]
    students[name] = scores

print("Students Data: ")
print(students)

for name, scores in students.items():
    student_average = average(scores)
    students[name].append(student_average)

print("Student's average: ")
print(students)

general_average: float = [average(notas) for notas in students.values()]
class_general_average: float = average(general_average)

print("General average: {:.2f}".format(class_general_average))


