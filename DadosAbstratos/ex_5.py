#Um consultório odontológico precisa gerenciar a ordem de atendimento dos
# pacientes. Para isso, foi decidido implementar uma fila onde os pacientes são
# chamados na ordem em que chegaram (FIFO – First In, First Out).



pacientes = []

while True:
    print("\nFila de atendimento:")
    for paciente in pacientes:
        print(paciente)
    if not pacientes:
        print("Vazia")
    
    opcao = input("[1] Adicionar Paciente | [2] Chamar Paciente | [3] Sair: ")
    
    if opcao == "1":
        nome = input("Digite o nome do paciente: ")
        pacientes.append(nome)
    elif opcao == "2":
        if pacientes:
            print(f"Paciente {pacientes.pop(0)} foi chamado.")
        else:
            print("Nenhum paciente na fila.")
    elif opcao == "3":
        break
