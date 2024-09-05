"""
ESCOLHENDO A OPÇÃO
"""

while True:
    print("\nMenu:")
    print("1. coxinha")
    print("2. pizza")
    print("3. hamburger")
    print("4. kibe")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == '0':
        print("Saindo...")
        break
    elif escolha == '1':
        print("Você escolheu  coxinha!!")
    elif escolha == '2':
        print("Você escolheu pizza!")
    elif escolha == '3':
        print("Você escolheu a hamburger!")
    elif escolha == '4':
        print("Você escolheu a kibe!")
    else:
        print("Opção inválida! Tente .")