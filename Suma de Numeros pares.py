#Aplica la fórmula de la suma de los primeros n números pares (investigar), 
# tomando como n la variable de tipo entero y almacenar el resultado en una variable

def sumar_numeros_pares(inicio, fin):
    suma = 0
    for num in range(inicio, fin + 1):
        if num % 2 == 0:
            suma += num
    return suma

inicio = int(input("Ingrese el numero de inicio del rango: "))
fin = int(input("Ingrese el número final del rango: "))

resultado = sumar_numeros_pares(inicio, fin)
print(f"La suma de los números pares entre {inicio} y {fin} es: {resultado}")
