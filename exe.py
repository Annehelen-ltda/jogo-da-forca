import random
from string import ascii_letters

temas = ["cores", "comidas", "desenhos"]
cores = ["azul", "vermelho", "violeta", "ciano"]
comidas = ["lasanha", "pastel", "farofa", "macaxeira"]
desenhos = ["ben 10", "she-ra", "the owl house", "bob o construtor"]

tema = random.choice(temas)
letras_escolhidas = []
tentativas = 6
acertos = 0
palavra_sorteada = ""
posicao = ""
        
print("Para fechar digite: END")
inicio = str(input("digite uma letra qualquer para iniciar ou encerre o jogo: ")).strip().lower()


if (inicio == "end"):
    print("Fim de jogo, bye bye")
else:
    print("deseja MESMO continuar? UAU... ok, né. Você tem 6 chances iniciais, boa sorte.")
    print("O tema é:", tema)
    
    if(tema == "cores"):
         palavra_sorteada = random.choice(cores)
    elif(tema == "comidas"):
        palavra_sorteada = random.choice(comidas)
    else:
        palavra_sorteada = random.choice(desenhos)
        
    #posicao = "_"*len(palavra_sorteada)
        
    for i in palavra_sorteada:
        if i in ascii_letters:
            posicao += "_"
        else:
            posicao += i
        
    print(posicao)
    
    letra = str(input("Você ta pronto? -sim ou não- ").lower())
    
    while "end" or "não" or "nao" not in letra:
        
        letra = str(input("Chuta uma letra aí: ").lower())
        
        if(letra == ""):
            print("letra invalida, tente novamente")
        else:
            if letra in letras_escolhidas:
                print("você já tentou essa letra fi")
                continue

            else:
                letras_escolhidas.append(letra)
                print("letras tentadas:", letras_escolhidas)
                    
        
        #print (palavra_sorteada)
        
        if letra in palavra_sorteada:
            
            for i in range(len(palavra_sorteada)):
                if palavra_sorteada[i] == letra:
                    posicao = posicao[:i] + letra + posicao[i+1:]
                    print(posicao)
                    acertos += 1     
            print("letra acertadas:", acertos)
                
        elif letra in ("end", "não", "nao", "parar"):
            print("bybye")  
            break       
        
        else:
            print("tente novamente")
            tentativas -= 1
            print("Menos -1 tentativa, restam:", tentativas)
            if(tentativas<0):
                print("Você perdeu")
                break
            
        if(palavra_sorteada == posicao):
            print("Temos um vencedor e....\nTU! Brabissimo!!!!!!! \nFizesse:", acertos, "pontos!" )
            break
        
print("até a proxima")


    