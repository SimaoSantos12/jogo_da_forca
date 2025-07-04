import random
from GanharPerder import ganhar
from GanharPerder import perder
from Boneco import forca

erradas=0
    
palavras = list(open('palavras.txt','r',encoding='utf-8'))

palavras = [s.rstrip() for s in palavras]

print("|———————————————————————————————————|")
print("|                                   |")
print("|   Bem vindo ao jogo da Forca!     |")
print("|                                   |")
print("|———————————————————————————————————|")

dificuldade=int(input('1-Fácil\n2-Normal\n3-Difícil\nSeleciona a dificuldade:'))
#print(palavras)

while dificuldade<1 or dificuldade>3:
    print("Essa opção não é válida!")
    dificuldade=int(input('1-Fácil\n2-Normal\n3-Difícil\nSeleciona a dificuldade:'))

if dificuldade == 1:
    palavra=random.choice(palavras)
    while len(palavra)>5:
        palavra=random.choice(palavras)
            
if dificuldade == 2:
    palavra=random.choice(palavras)
    while len(palavra)<6 or len(palavra)>7 :
        palavra=random.choice(palavras)
            
if dificuldade == 3:
    palavra=random.choice(palavras)
    while len(palavra)<8:
        palavra=random.choice(palavras)

arrayComTracos=[]
arrayComPalavra=list(palavra)
arrayLetrasErradas=[]

for x in palavra:
    arrayComTracos.append('_')

print()
print("A palavra possui:",len(arrayComTracos),"letras. Boa sorte!")
print()
#print(palavra)

t=0
acabou=0
while t==0:
    contador=0

    print(*arrayComTracos) 

    print()
    letra=input("Digita uma letra ou tenta adivinhar a palavra:")
    
    while len(letra)!=1 and len(letra)>len(arrayComTracos) or len(letra)!=1 and len(letra)<len(arrayComTracos):
        print("Essa opçâo não e válida!")
        print()
        print(*arrayComTracos)
        letra=input("Digita uma letra:")

    if len(letra)==len(arrayComTracos):
        if letra!=palavra:
            print()
            perder()
            print()
            print('A palavra era:',palavra)
            t=1
        else:
            t=1
            print()
            ganhar()
            
    else:

        for x in arrayComPalavra:
            contador=contador+1
            if letra == x:
                index=contador-1
                arrayComTracos[index]=letra
            
        if letra not in arrayComPalavra:
            if letra not in arrayLetrasErradas:
                erradas=erradas+1
                if dificuldade!=3:
                    arrayLetrasErradas.append(letra)
       
    if erradas>0:
        print()
        forca(erradas)
        if dificuldade!=3:
            print('Letras erradas:',*arrayLetrasErradas)

    print()

    if erradas ==5:
        acabou=1
        t=1
        print()
        perder()
        print()
        print('A palavra era:',palavra)
    if arrayComPalavra==arrayComTracos:
        t=1
        acabou=1
        print()
        ganhar()