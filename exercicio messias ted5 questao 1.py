n1= float(input("Digite a primeira nota: "))
n2= float(input("Digite a segunda nota: "))
n3= float(input("Digite a terceira nota: "))

m =(n1 + n2 + n3) /3
print("O Valor da média aritimétrica entre {}, {} e {} é igual a {}".format(n1,n2,n3,m))

if m >=7:
    print("Parabéns!!!")
else:
    print("Precisa estudar um pouco mais!")