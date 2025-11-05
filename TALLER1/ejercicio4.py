# Solicitar el área original
areaOriginal = int(input("Ingrese el área original del terreno : "))

# Reducción del 10%
reduccion = areaOriginal * 0.10
areaReducida = areaOriginal - reduccion

# Aumento del 50% sobre el área reducida
aumento = areaReducida * 0.50
areaTotal = areaReducida + aumento

# Mostrar resultados

print(f"Área original: {areaOriginal} ")
print(f"Reducción (10%): -{reduccion} ")
print(f"Área después de la reducción: {areaReducida:.2f} ")
print(f"Aumento (50%): +{aumento} ")
print(f"Área total final: {areaTotal}")