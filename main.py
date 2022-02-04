from conta import Conta
from cabecalho import Cabecalho
import cliente

Cabecalho()

while True:
    conf = int(input("Opção: "))
        
        
    if conf == 1:
        print("Cadastro de clientes\n")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        idade = input("Idade: ")
        cliente.Cliente(nome, cpf, idade)
        print("Cadastrado com sucesso.")
        Cabecalho()
            
            
    if conf == 2:
        print(f"Qual cliente quer consultar?\n")
        for k in cliente.usuarios:
            print(f"{k} - {cliente.usuarios[k][0]}")
        opc = int(input("\nOpção: "))
        print(f"\nNome: {cliente.usuarios[opc][0]}\nCPF: {cliente.usuarios[opc][1]}\nIdade: {cliente.usuarios[opc][2]}\n")
        Cabecalho()
    
    
    if conf == 3:
        print("Até mais")
        break
