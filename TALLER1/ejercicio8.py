# Solicitar costos
llamada1 = float(input("Costo de la primera llamada (operador 1): "))
llamada2 = float(input("Costo de la segunda llamada (operador 1): "))
llamada3 = float(input("Costo de la primera llamada (operador 2): "))
llamada4 = float(input("Costo de la segunda llamada (operador 2): "))

# Calcular totales
total_op1 = llamada1 + llamada2
total_op2 = llamada3 + llamada4
total_general = total_op1 + total_op2

# Mostrar resultados
print(f"Costo total operador 1: ${total_op1}")
print(f"Costo total operador 2: ${total_op2}")
print(f"Costo total de las 4 llamadas: ${total_general}")
