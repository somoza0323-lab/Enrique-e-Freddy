meses = ("Janeiro", "Fevereiro", "Março", "abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Desembro")  

num = int(input("Digite um numero de 1 a 12: "))

if 1 <= num <= 12:
    print(meses[num - 1])
else:
    print("Numero invalido!")