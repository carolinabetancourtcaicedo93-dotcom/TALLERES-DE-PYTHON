# Solicitar costos
llamada1 = float(input("Costo de la primera llamada (operador 1): "))
llamada2 = float(input("Costo de la segunda llamada (operador 1): "))
llamada3 = float(input("Costo de la primera llamada (operador 2): "))
llamada4 = float(input("Costo de la segunda llamada (operador 2): "))

# Calcular totales
totalOp1 = llamada1 + llamada2
totalOp2 = llamada3 + llamada4
totalGeneral = totalOp1 + totalOp2

# Mostrar resultados
print(f"Costo total operador 1: ${totalOp1}")
print(f"Costo total operador 2: ${totalOp2}")
print(f"Costo total de las 4 llamadas: ${totalGeneral}")
