saldo_inicial = 1000
print(f"Saldo: ${saldo_inicial}")

operaciones = int(input("Cuantas operaciones desear realizar: "))

for i in range(operaciones):
    print("\n--MENU--")
    print("-1 Consultar saldo-")
    print("-2 Retirar dinero-")
    print("-3 Depositar dinero-")

opcion = int(input("Debe elegir una opcion: "))

if opcion == 1:
    print(f"Su saldo actual es de: ${saldo_inicial}")

elif opcion == 2:
    monto = int(input("Digite el monto a retirar: "))
    
    if monto > 0:
        print("Monto invalido")

    elif monto > saldo_inicial:
        print("Fondos insuficientes")
    else:
        saldo = saldo_inicial - monto
        print("Retiro exitoso")
        print(f"Nuevo saldo: ${saldo}")

elif opcion == 3:
    monto1 = float(input("Escribir monto a depositar: "))
    
    if monto < 0:
        print("Monto invalido")
    
    else:
        saldo1 = saldo_inicial + monto
        print("Retiro exitoso")
        print(f"Nuevo saldo: {saldo1}")

else:
    print("Opcion invalida")


print("GRACIAS POR EL USAR EL CAJERO AUTOMATICO")