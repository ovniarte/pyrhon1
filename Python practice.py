#Tipos de Datos Variables de tipo Primitivo 
Numero_Entero = 12
Numero_Reales = 1.76
Nombre_Apellido = "Juan"
Apellido = "Valdez"
Genero_M = True

# Ejercicio de Cadena con Variables de Tipo primitivo y concatenacion de las mismas
Perfil= Nombre_Apellido + Apellido + str(Numero_Entero)
print("Hola mi nombres es " + Nombre_Apellido + " " + "y mi apellido es"+" " + Apellido)

#¿Cómo de grande puede ser un int (Numero entero) en Python? La respuesta es de cualquier tamaño. 
# En cambio los numeros Flotantes La mínima precisión es 2.2250738585072014e-308 y la máxima 1.7976931348623157e+308

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

