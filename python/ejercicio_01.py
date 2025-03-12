"""
    Programa que escribe los pares menores o iguales que un número introducido (usar promt),
    este debe ser positivo y mayor que 2.

    Muestralos por consola.

    Extra:  Y que sean mayor que 2.
"""

def obtener_resultados(number):
    num = 0
    while num <= number:
        if num % 2 == 0 and num > 2:
            result.append(num)
        num += 1

    return result


result = []
input_number = int(input("Introduce un número: "))
result = obtener_resultados(input_number)

print(f"Resultado: {result}")
