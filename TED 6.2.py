ano1=int (input("Digite o ano corrente: "))
ano2=int (input("Digite o ano em que você nasceu: "))
r = ano1 - ano2
if r >= 16:
    print("Você pode votar!")
else:
    print("Você ainda não pode votar!")
