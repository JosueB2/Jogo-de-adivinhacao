import Forca
import Adivinhação

def escolher_jogo():
    print('********************************')
    print('******!Escolha um jogo!*********')
    print('********************************')
    
    print('(1) Forca (2) Adivinhação')
    
    jogo = int(input('Qual jogo?'))
    
    if(jogo == 1):
      print('Jogando Forca') 
      Forca.jogar()
    else:
      print('Jogando Adivinhação')
      Adivinhação.jogar()
 
if(__name__ == "__main__"):
 escolher_jogo()      