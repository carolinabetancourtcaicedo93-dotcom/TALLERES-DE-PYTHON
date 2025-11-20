#Una empresa quiere hacer una compra de varias piezas de la misma clase a una fábrica de
#bolsos. La empresa, dependiendo del monto total de la compra, decidirá qué hacer para
#pagar al fabricante:

#Si el monto total de la compra excede de $500 000 la empresa tendrá la capacidad
#de invertir de su propio dinero un 55% del monto de la compra, pedir prestado al
#banco un 30% y el resto lo pagará solicitando un crédito al fabricante.

#Si el monto total de la compra no excede de $500 000 la empresa tendrá capacidad
#de invertir de su propio dinero un 70% y el restante 30% lo pagará solicitando
#crédito al fabricante. El fabricante cobra por concepto de intereses un 20% sobre
#la cantidad que se le pague a crédito.

#Imprimir el valor invertido de su propio dinero, el valor prestado al banco, y el valor del crédito
#solicitado al fabricante, según sea el caso.

monto = float(input("Ingrese el monto total de la compra: "))

if monto > 500000:
    inversion = monto * 0.55
    prestamo = monto * 0.30
    credito = monto * 0.15
    
    print(f"Inversión propia: ${inversion:,.2f}")
    print(f"Préstamo bancario: ${prestamo:,.2f}")
    print(f"Crédito al fabricante: ${credito:,.2f}")

else:
    inversion = monto * 0.70
    credito = monto * 0.30
    interes = credito * 0.20
    total_credito = credito + interes

    print(f"Inversión propia: ${inversion:,.2f}")
    print(f"Crédito al fabricante: ${credito:,.2f}")
    print(f"Interés al fabricante: ${interes:,.2f}")
    print(f"Total a pagar al fabricante: ${total_credito:,.2f}")






