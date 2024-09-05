"""
SOMANDO OS DÍGITOS
"""

while True:
    numero = input("Digite um número inteiro (ou 0 para sair): ")
    if numero == "0":
        break
    
    soma_digitos = sum(int(digito) for digito in numero)
    """
    a variavel soma de digitos recebe uma função de soma onde cada
    digito contido em um nunero é somado com outro
    """
    print(f"A soma dos dígitos de {numero} é {soma_digitos}")
    """
    exibe o numero digitado e a soma de todos os digitos deste mesmo numero
    """