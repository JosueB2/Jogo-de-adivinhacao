import random

def jogar():
    
    print('********************************')
    print('Bem-vindo ao Jogo de adivinhação')
    print('********************************')
    
    tentativas = 0
    numero_secreto = random.randrange(1,101) 
    fim = str(numero_secreto)
    pontos = 1000
    
    
    print('Qual nível de dificuldade?')
    print('[1] Fácil [2] Médio [3] Difícil')
       
    nivel = int(input('Nível escolhido: '))
    
    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5   
        
    for rodada in range(1, tentativas +1):
    
         print(' Tentativa {} de {}'. format(rodada, tentativas))
         chute_str = input(' Escolha um número entre 1 e 100: ')
         chute = int(chute_str)
         
         if(chute < 1 or chute > 100):
             print(' Use apenas números positivos entre 1 e 100')
             continue
         
         chute_menor = chute < numero_secreto
         chute_maior = chute > numero_secreto
         acertou = chute == numero_secreto 
    
         if(acertou):
           print(' Parabens! Você acertou')
           break 
         else:
            if(chute_maior):
               print(' Você errou!!! Seu número foi acima do número secreto')
          
           
            elif(chute_menor):
              print(' Você errou!!! Seu número foi abaixo do número secreto')
              pontos_perdidos = abs(numero_secreto - chute)
              pontos = pontos - pontos_perdidos
              pontos_str = str(pontos)
              
    print(' Fim de jogo')
    print(' O número secreto era:' + fim)
    print(' Total de pontos:' + pontos_str)


    
      
        
if(__name__ == "__main__"):
 jogar()      