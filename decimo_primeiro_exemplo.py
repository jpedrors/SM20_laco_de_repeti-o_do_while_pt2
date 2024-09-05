print("TABUADA")

while True:
    numero = int(input("Digite um número para ver a tabuada (0 para sair): "))
    if numero == 0:
        break  # Corrigir indentação aqui

    for i in range(1, 11):  # Início do loop para gerar a tabuada
        print(f"{numero} x {i} = {numero * i}")  # Corrigir indentação aqui
