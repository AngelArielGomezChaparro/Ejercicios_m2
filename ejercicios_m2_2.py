try:
    numero = int(input("Ingrese un número: "))

    
    if numero % 2 == 0:
        print(f"Su número {numero} es par.")

    
    elif numero == 7:
        print(f"¡Jo! El número de la suerte, por cierto, es impar.")

    
    else:
        print(f"Su número {numero} es impar.")

except ValueError:
    print("Por favor, ingrese un número entero válido.")
