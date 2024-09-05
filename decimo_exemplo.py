"""
CALCULANDO A MÉDIA DAS NOTAS
"""
soma = 0
contagem = 0

while True:
    nota = float(input("Digite uma nota (ou -1 para terminar): "))
    if nota == -1:  # Se digitar -1, encerra o programa
        break
    soma += nota  # Soma as notas inseridas
    contagem += 1  # Conta a quantidade de notas para calcular a média

if contagem > 0:
    media = soma / contagem
    media_arredondada = round(media, 2)  # Arredonda a média para 2 casas decimais
    print(f"A média das notas é: {media_arredondada}")
else:
    print("Nenhuma nota foi inserida.")
