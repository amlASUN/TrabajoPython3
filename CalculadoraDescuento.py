# Cabecera
# CalculadoraDescuentos
# Autores: Aitor y Jaime
# Fecha: 01/10/2026 

Descuento1 = 0.10 # Valor de descuento 10%
Descuento2 = 0.15 # Valor de descuento 15%
Precio = float(input("Introduce el precio del producto a calcular:")) # Float para poder usar números con comas e integrar al programa el dato.
if Precio >= 300: # Descuento de 15% aplicado
    PrecioTotal = Precio - (Precio*Descuento2)
    PrecioDescontado = Precio*Descuento2
    print("El precio aplicado tiene un 15% descuento.")
    print(f"El descuento es de: {PrecioDescontado} €")
    print(f"El precio final es de: {PrecioTotal} €")

elif Precio >= 100 and Precio < 300: # Descuento de 10% aplicado
    PrecioTotal = Precio - (Precio*Descuento1)
    PrecioDescontado = Precio*Descuento1
    print("El precio aplicado tiene un 10% descuento.")
    print(f"El descuento es de: {PrecioDescontado} €")
    print(f"El precio final es de: {PrecioTotal} €")

else: # Descuento no aplicado
    print("El descuento no aplica.")
    print(f"El precio final es de: {Precio} €")
 
# EJERCICIO 
# Una tienda aplica un descuento del 10 % a partir de 100 € de compra y 
# del 15 % a partir de 300 €. Recorred las cinco fases del capítulo 2: 
# análisis (documentad entradas, salidas y restricciones), diseño (pseudocódigo y ordinograma), 
# codificación en Python, pruebas (tabla con al menos seis casos, incluidos 
# los límites 99,99 €, 100 € y 300 €) y documentación (cabecera y comentarios según PEP 8).
# Entrega: repositorio Git con el código y un README.md con el resto.