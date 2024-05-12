#programa com o objetivo de identificar se determinada letra é vogal ou consoante
letra = str(input("digite a vogal ou consoante"))

if(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"): #condição para realizar os comandos dentro do if se for verdadeira
    print("a letra digitada trata-se de uma vogal ")
else:#se a condição for falsa o bloco else será executado
    print("a letra é consoante")