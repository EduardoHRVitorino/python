var = float(input("digite um valor: "))
porcentagem = float(var - (var * 5) / 100) 
print("preço anterior:{:.2f} descontando 5% vira {:.2f}" .format(var, porcentagem))