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

print("Ingrese valor Inicial")
i = int(input())
print("Ingrese el numero fnal")
f = int(input())
suma = 0
print(" **Los numeros pares del Rango**")
while i <= f:
    if i % 2 == 0:
        print(i)
      i+=1