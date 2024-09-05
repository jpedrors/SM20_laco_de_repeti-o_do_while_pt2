"""
CONTAGEM REGRESSIVA
"""
while True:
    numero = int(input("Digite um número para iniciar a contagem regressiva: "))
    
    while numero >= 0: # enquanto for maior que 0 
        print(numero) # mostre o numero  
        numero -= 1 # na ordem decrescente
    
    continuar = input("Quer fazer outra contagem regressiva? (sim/nao): ")
    if continuar.lower() == 'nao': # se digitar "nao"
        break # vai parar