# Preguntar al usuario por la edad
edad = int(input("Por favor, ingresa tu edad: "))

# Calcular el precio de entrada
if edad < 4:
    precio = 0  # Menores de 4 años entran gratis
elif edad <= 18:
    precio = 5  # De 4 a 18 años pagan 5 monedas
else:
    precio = 10  # Mayores de 18 años pagan 10 monedas

# Mostrar el precio de entrada al usuario
print(f"El precio de entrada es de {precio} monedas.")
