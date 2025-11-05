# Solicitar medidas
alto = float(input("Ingrese el alto del muro (m): "))
ancho = float(input("Ingrese el ancho del muro (m): "))

# Calcular área y cajas necesarias
area = alto * ancho
cajas = area / 3.5

# Mostrar resultados
print(f"Área total: {area:.2f} m²")
print(f"Cajas necesarias: {cajas:.2f} (aproximadamente {round(cajas)} cajas)")
