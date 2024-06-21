salario = float(input("digite seu salário: R$"))
aumento = float(salario + (salario * 15 / 100))
print("o aumento do salario R${:.2f} de 15%, fica R${:.2f}".format(salario, aumento))