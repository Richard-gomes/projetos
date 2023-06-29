#ler 5 notas e fazer a media#
N1 = int(input('digite aqui a sua nota 1'))
N2 = int(input('digite aqui a sua nota 2'))
N3 = int(input('digite aqui a sua nota 3'))
N4 = int(input('digite aqui a sua nota 4'))
N5 = int(input('digite aqui a sua nota 5'))
print ('Sua nota é', (N1+N2+N3+N4+N5)/5)
#com for
nota=media=soma=0
for _ in range(1, 6):
    nota=float(input('digite sua nota'))
    soma+=nota
print (soma)
media=soma/5
print ('A sua media é', media)
#com while
numero=1
while numero <= 5:
    nota=float(input('digite sua nota'))
    soma+=nota
    numero+=1
print('sua media é', soma/5)