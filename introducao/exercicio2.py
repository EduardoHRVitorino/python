a = float(input("digite o valor do lado <A>:"))
b = float(input("digite o valor do lado <B>:"))
c = float(input("digite o valor do lado <C>:"))

if(a < b + c and b < a + c and c < a + b):

    if(a == b and b == c):
        print("o triângulo é equilátero")
    else:
        if(a == b or b == c or c == a):
            print("o triangulo é isósceles")
        else:
            print("triângulo escaleno")
else:
    print("os valores não correspondem a um triangulo")
