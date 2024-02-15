import os
import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    
    arquivo=open(f'{os.getcwd()}\\teste.txt','r')
    palavras=[]
    for l in arquivo:
        l=l.strip()
        palavras.append(l.strip())
    aleatorio=random.randrange(0, len(palavras))
    arquivo.close()
    
    palavra_secreta=palavras[aleatorio].upper()
    enforcou=False
    acertou=False
    linhas=['_'] * len(palavra_secreta)
    tentativas=0
    
    while (not enforcou and not acertou):
        index=0
        chute=input('Qual letra?: ').upper().strip()
        if chute in palavra_secreta:
            for letra in palavra_secreta:
                if chute == letra:
                    linhas[index]=letra
                index +=1    
        else:
            tentativas+=1
            #print(tentativas)
        enforcou= tentativas == len(palavra_secreta)
        acertou='_' not in linhas
        print(linhas)
    if acertou:
            print('Você ganhou!!!')
    else:
            print('Você perdeu')
           
        
if(__name__ == "__main__"):
    jogar()