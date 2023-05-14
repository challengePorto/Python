def cadastro():
    print("==========================")
    cpf = input("digite o CPF: ")
    nome = input("digite o nome: ")
    senha = input("digite a senha: ")
    
def login():
    cpf = input("digite o CPF: ")
    senha = input("digite a senha: ")

def planos():
    print("=========consulta de Planos=========")
    print("Plano A \nPlano B \nPlano C")

def solicitar_guincho():
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

if __name__ == '__main__':
    while True:
        resposta = int(input('1 - cadastrar usuario \n2 - login \n3 - consultar plano \n4 - solicitar guincho \n5 - sair\n'))
        
        if resposta == 1:
            cadastro()
        elif resposta == 2:
            login()
        elif resposta == 3:
            planos()
        elif resposta == 4:
            solicitar_guincho()
        elif resposta == 5:
            break
        else:
            print("opcao incorreta")