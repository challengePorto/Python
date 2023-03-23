print('1 - cadastrar usuario \n2 - login \n3 - consultar plano \n4 - solicitar guincho')

resposta_continuar = 'SIM'

while resposta_continuar == "SIM":
    resposta = int(input('1 - cadastrar usuario \n2 - login \n3 - consultar plano'))
    if resposta == 1:
        print("=========cadastre o usuario=========")
        usuario_cadastro = input('digite o nome do usuario: ')
        email_cadastro = input('digite o email: ')

    elif resposta == 2:
        print("=========Login=========")
        usuario_login = input('digite o nome do usuario: ')
        email_login = input('digite o email: ')

    elif resposta == 3:
        print("=========consulta de Planos=========")
        print("Plano A \nPlano B \nPlano C")

    elif resposta == 4:
        print("=========solicitar guincho=========")
        cpf = input("digite seu CPF: ")
        peso_caminhao = float(input("Quantos KG deu caminhao esta?"))
        cidade = input("digite a cidade: ")
        rua_rodovia = input("digite a rua ou rodovia: ")

        print("selecione o tipo de carga: \na granel \nfrigorífico \ncarga viva \nperigosas \nsecas")
        tipo_carga = int(input('selecione uma carga: '))

        print("=========Informacao de problema=========")
        print("selecione o tipo de carga: \nsem funcionamento do motor \nsem sinal eletrico \ntombou \npneu")
        tipo_problema = int(input("selecione o problema"))
    else:
        print("opcao incorreta")
        resposta = int(input('1 - cadastrar usuario \n2 - login \n3 - consultar plano'))
        
    resposta_continuar = input("Deseja continuar? (sim/nao)").upper()




