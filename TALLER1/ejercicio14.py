# Ingresar notas
taller1 = float(input("Taller 1: "))
taller2 = float(input("Taller 2: "))
eval1 = float(input("Evaluación 1: "))
eval2 = float(input("Evaluación 2: "))
eval3 = float(input("Evaluación 3: "))
trabajoFinal = float(input("Trabajo final: "))
quiz1 = float(input("Quiz 1: "))
quiz2 = float(input("Quiz 2: "))
quiz3 = float(input("Quiz 3: "))
quiz4 = float(input("Quiz 4: "))

# Calcular ponderaciones
nota1 = ((taller1 + taller2) / 2) * 0.15
nota2 = ((eval1 + eval2 + eval3) / 3) * 0.30
nota3 = trabajoFinal * 0.30
nota4 = ((quiz1 + quiz2 + quiz3 + quiz4) / 4) * 0.25
definitiva = nota1 + nota2 + nota3 + nota4

# Mostrar resultado
print(f"Nota definitiva: {definitiva:.2f}")