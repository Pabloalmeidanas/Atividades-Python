from wsgiref.validate import validator


lista=[[],[]]
numero=0
for i in range(1,6):
    numero=int(input("Digite um número -> "))
    if (numero%2)==0:
        lista[0].append(numero)

    else:
        lista[1].append(numero)
print(f"Os numeros {lista[0]} são pares")
print(f"os numeros {lista[1]} são ímpares")
        
   