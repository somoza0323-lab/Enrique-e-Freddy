# 5. Encontrar o maior valor da matriz 3x3.

matriz = []
maior = None

for i in range(3):
    linha = []
    for j in range(3):
     valor = int(input(f"Digite o valor para [{i}][{j}]:"))
     linha.append(valor)

     if maior is None or valor > maior:
        maior = valor

    matriz.append(linha)

print("Maior valor =", maior)