# Ingresar datos de los 3 días
tiempo1 = float(input("Tiempo día 1 (min): "))
distancia1 = float(input("Distancia día 1 (m): "))
tiempo2 = float(input("Tiempo día 2 (min): "))
distancia2 = float(input("Distancia día 2 (m): "))
tiempo3 = float(input("Tiempo día 3 (min): "))
distancia3 = float(input("Distancia día 3 (m): "))

# Calcular totales y promedios
total_tiempo = tiempo1 + tiempo2 + tiempo3
total_distancia = distancia1 + distancia2 + distancia3
prom_tiempo = total_tiempo / 3
prom_distancia = total_distancia / 3

# Mostrar resultados
print(f"Tiempo total: {total_tiempo} minutos")
print(f"Distancia total: {total_distancia} metros")
print(f"Promedio de tiempo: {prom_tiempo:.2f} min")
print(f"Promedio de distancia: {prom_distancia:.2f} m")
