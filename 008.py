km = float(input("qual a quantidade de km rodados: "))
dias = float(input("por quantos dias voce rodou?: "))
pago = (dias * 60) + (km * 0.15)
print("a sua conta é R${:.2f}".format(pago))