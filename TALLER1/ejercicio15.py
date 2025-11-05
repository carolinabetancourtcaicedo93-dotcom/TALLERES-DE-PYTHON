# Ingresar datos
inicio = int(input("Número inicial del contador: "))
fin = int(input("Número final del contador: "))
valor_pasaje = float(input("Valor del pasaje: "))

# Calcular resultados
pasajeros = fin - inicio
total = pasajeros * valor_pasaje
empresa = total * 0.75
conductor = total * 0.25

# Mostrar resultados
print(f"Pasajeros transportados: {pasajeros}")
print(f"Total recaudado: ${total}")
print(f"Empresa recibe: ${empresa}")
print(f"Conductor recibe: ${conductor}")