# Ingresar datos de los 3 días
tiempo1 = float(input("Tiempo día 1 (min): "))
distancia1 = float(input("Distancia día 1 (m): "))
tiempo2 = float(input("Tiempo día 2 (min): "))
distancia2 = float(input("Distancia día 2 (m): "))
tiempo3 = float(input("Tiempo día 3 (min): "))
distancia3 = float(input("Distancia día 3 (m): "))

# Calcular totales y promedios
totalTiempo = tiempo1 + tiempo2 + tiempo3
totalDistancia = distancia1 + distancia2 + distancia3
promTiempo = totalTiempo / 3
promDistancia = totalDistancia / 3

# Mostrar resultados
print(f"Tiempo total: {totalTiempo} minutos")
print(f"Distancia total: {totalDistancia} metros")
print(f"Promedio de tiempo: {promTiempo:.2f} min")
print(f"Promedio de distancia: {promDistancia:.2f} m")
