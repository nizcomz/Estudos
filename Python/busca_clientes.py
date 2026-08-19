
def login_check(credentials):
    while True:
        if credentials_bd in credentials:
            print("Acesso Permitido")
            return True
        break
    else:
        print("Acesso negado !"
        "\nTente novamente !")
        return None

def search_clients(serch):
    for clients in serch:
        for clients 



credentials_bd = [
    {"login": "admin"},
    {"passwor": "1234"}
]

clients = [
    {"id": 1, "nome": "Maria Silva", "telefone": "31 99999-9999", "procedimento": "Limpeza de pele"},
    {"id": 2, "nome": "João Santos", "telefone": "31 98888-8888", "procedimento": "Microagulhamento"},
    {"id": 3, "nome": "Ana Costa", "telefone": "31 97777-7777", "procedimento": "Drenagem Linfática"},
    {"id": 4, "nome": "Pedro Oliveira", "telefone": "31 96666-6666", "procedimento": "Massagem Relaxante"}
]

while True:
    login = input("Por favor, digite seu login: ")
    password = input("Por favor digite sua senha: ")
    login_check(login, password)

    choice = input("\nBem vindo ao BD Clinica"
                    "\nEscolha uma opção de consulta"
                    "\n(1) Consultar procedimentos disponíveis" 
                    "\n(2) Consultar Cadastros"
                    "\n(3) Sair")

    if choice == "3":
        print("\nBanco de dados encerrado !"
              "\nVolte Sempre")
        break

    if choice == "2":
        client_name = input("Digite o nome do cliente que deseja consultar: ")
            name_serch = search_clients(client_name)


    





   










