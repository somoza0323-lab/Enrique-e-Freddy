soma = 0
quantidade = 0

num = int(input("Digite um numero (0 para sair): "))

while num != 0:
    soma += num
    quantidade+= 1
    num = int(input("Digite um numero (0 para sair): "))

print("Quantidade:", quantidade)
print("Soma:", soma)