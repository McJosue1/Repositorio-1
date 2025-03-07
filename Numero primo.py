#verificar si es numero primo
n= int(input( "Ingresa el numero que quieras verificar we:" ))
primo = True
for i in range (2 , n-1):
    if (n % i)==0:
        primo = False
print ("El numero", n , "es primo", primo)