#faça um programa para calcular um fatorial de um numero qualquer
n= int(input("digite o número"))
if n > 0:
    fatorial=1
    for item in range(1,n+1):
        fatorial=fatorial*item
        print(fatorial)
        