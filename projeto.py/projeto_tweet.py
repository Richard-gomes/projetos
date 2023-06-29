#DESAFIO
#O microblog Twitter é conhecido por limitar as postagens em 140 caracteres
#A saída é dada em uma única linha. Ela deve ser "TWEET" (sem as aspas) se a linha de texto T tem até 140 caracteres. Se T tem mais de 140 caracteres, a saída deve ser "MUTE".
def minhaClasse():
    tweet = input()
    arr = list(tweet)
    
    if len(arr) <= 140:
        print("TWEET")
    else:
        print("MUTE")

minhaClasse()