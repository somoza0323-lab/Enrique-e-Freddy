soma = 0

for i in range(5):
    num = float(input(f"Digite {i+1}° numero: "))
    soma += num

media = soma / 5

print("Soma:", soma)
print("Média:", media)