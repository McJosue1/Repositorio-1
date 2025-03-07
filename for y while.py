# Verificar si es número primo
n = int(input("Ingresa el numero que quieras verificar we: "))
primo = True

for i in range(2, n):
    if n % i == 0:
        primo = False
        while  # Si encontramos un divisor, no es primo y se sale del bucle

if primo:
    print("El numero", n, "es primo")
else:
    print("El numero", n, "no es primo")