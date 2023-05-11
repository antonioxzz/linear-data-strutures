"""
Ejercicio de conversión de unidades: Escribe un programa que convierta una cantidad en una unidad 
de medida a otra unidad de medida utilizando un diccionario para almacenar las relaciones de conversión.
"""
def convert_units(amount: float, unit_source: str, unit_target: str, conversion: dict) -> float:
    """Convierte una cantidad de una unidad de medida a otra, utilizando un diccionario de conversiones."""
    conversion_factor = conversion[unit_source][unit_target]
    target_amount = amount * conversion_factor
    return target_amount


conversion = {
    "meters": {"pies": 3.28084, "inches": 39.3701},
    "foot": {"meters": 0.3048, "inches": 12},
    "inches": {"meters": 0.0254, "feet": 0.0833333}
}

amount = float(input("Enter the amount: "))
unit_source: str = input("Enter source amount: ")
unit_target: str = input("Enter target amount: ")

target_amount: float = convert_units(amount, unit_source, unit_target, conversion)

print(f"{amount} {unit_source} equivale a {target_amount} {unit_target}")

