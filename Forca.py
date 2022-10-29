import random

def jogar():
    
    tela_inicial()
     
    palavra_secreta = carregamento_palavra_secreta()
    
    letras_corretas = inicializa_quantas_palavras(palavra_secreta)
    
    print(letras_corretas)    
       
    enforcou = False
    acertou = False
    erros = 0
            
    while (not acertou and not enforcou):

        chute = pede_chute()
        
        if(chute in palavra_secreta):          
           marca_ponto_correto(chute, palavra_secreta, letras_corretas)
                                   
        else: 
            erros += 1
            desenha_forca(erros)
            
        enforcou = erros == 7    
        acertou = "_" not in letras_corretas        
        print(letras_corretas)
        
    if (acertou):
        imprime_mensagem_vitoria()
    else:
        imprime_mensagem_derrota(palavra_secreta)

def tela_inicial():  
    
    print('********************************')
    print('***Bem-vindo ao Jogo da forca***')
    print('********************************')

def carregamento_palavra_secreta():

    arquivo = open("Frutas.txt", "r")
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo2 = open("Nomes.txt", "r")
    palavras = []
    
    for linha2 in arquivo2:
        linha2 = linha2.strip()
        palavras.append(linha2)
        
    arquivo.close()
    arquivo2.close()
    
    numero = random.randrange(0, len(palavras)) 
    
    palavra_secreta = palavras[numero].upper()
    
    return palavra_secreta

def imprime_mensagem_vitoria():
    print("PARABÉNS, VOCÊ GANHOU!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")   
            
def imprime_mensagem_derrota(palavra_secreta):
    
    
    print("     FIM DE JOGO      ")
    print("A palavra era {}". format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    
def inicializa_quantas_palavras(palavra):
    
    return ["_" for letra in palavra]

def pede_chute():
    
    chute = input("Qual letra? ")
    
    chute = chute.strip().upper()
    
    return chute
                    
def marca_ponto_correto(chute, palavra_secreta, letras_corretas):
    
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_corretas[index] = letra
            
        index += 1
        
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()   
    
if(__name__ == "__main__"):
    jogar()    