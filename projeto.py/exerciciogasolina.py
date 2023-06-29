#faz 12km por litro, o usuário deve fornercer o tempo fasto e a velocidade media durante o trajeto#
tempo_gasto = int(input('Quantos tempo (em horas) levou para percorrer o trajeto?'))
velocidade_media = int(input("Qual foi a sua velocidade media durante o trajeto (Em kilometros por hora)"))
distancia = int(velocidade_media*tempo_gasto)
litros_usados = int(distancia/12)

print('Você levou',tempo_gasto, 'horas.')
print('Sua velocidade média foi de', velocidade_media, 'kilometros por hora')
print('Você percorreu',distancia,'kilometros')
print('E o seu gasto de combustivel foi',litros_usados,'litros')