#Cree una lista vacía  denominada aprendices y edades
aprendices = []
edades = []

# llénelas solicitando los datos por teclado
cantidad = int(input("¿cuantos aprendices deseas ingresar?"))

for i in range(cantidad):
    nombre = input("nombre del aprendiz:" )
    edad = input("ingresa la edad del aprendiz:")
    aprendices.append(nombre)
    edades.append(edad)
    
    #Imprima las listas
    print(f"lista de aprendices: {aprendices}")
    print(f"lista de edades: {edades}")

    #Muestre el aprendiz con la mayor edad
    mayorEdad = max(edades)
    posicion = edades.index(mayorEdad)
    print(f"El aprendiz con mayor edad es: {aprendices[posicion]} con {mayorEdad} años")

    #Inserte el nombre de la instructora en la posición 1
    instructora = "instructora"
    aprendices.insert(1, instructora)
    print(f"lista depues de agregar instructora: {aprendices}")

    #contar cuantos aprendices tienen 18 años
    cantidad18 = edades.count(18)
    print(f"aprendices con 18 años de edad: {cantidad18}")

    #Agregue un aprendiz “x” al final de la lista
    aprendices.append("Diana")
    print(f"esta es la lista despues de agrgar a Diana: {aprendices}")

    #Borre el nombre de la instructora de la lista
    aprendices.remove(instructora)
    print(f"esta es la lista despues de eliminar a instructora: {aprendices}")

    #buscar un dato en la lista
    buscar = input("ingrese un nombre para buscar en la lista")
    if buscar in aprendices: 
     print("si se encuentra en la lista")
    else:
       print("no se encuentra en la lista")

    #Muestre los primeros 10 aprendices de la lista
    print(f"mostrar los primeros 10 aprendices: {aprendices[:10]}")

    #Muestre los 10 últimos aprendices de la lista
    print(f"mostrar los ultimos 10 aprendices: {aprendices[-10:]}")

    #Muestre del elemento 10 al elemento 20
    print(f"mostrar del 10 al 20: {aprendices[10:21]}")

    #Muestre los elementos de la lista, cuyo índice sea par
    
    print("elementos con indice par")
    par=[]
    for i in range(len(aprendices)):
       if i % 2 == 0 :
          par.append(aprendices[i])
          print(par)