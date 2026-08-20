
def login_check(credentials):
        if "admin" in credentials and "1234" in credentials:
            print("Acesso Permitido")
            return True
        else:
            print("Acesso negado !"
            "\nTente novamente !")
            return None

def search_clients(name):
    for cleint in clients:
         if clients["Nome"].lower() == name.lower():
              return name         
    return None
         
clients = [
    {"id": 1,
      "Nome": "Maria Silva",
      "Telefone": "31 99999-9999",
        "Procedimento": "Limpeza de pele"},

    {"id": 2,
      "Nome": "João Santos",
        "Telefone": "31 98888-8888",
          "Procedimento": "Microagulhamento"},

    {"id": 3,
      "Nome": "Ana Costa",
        "Telefone": "31 97777-7777",
          "Procedimento": "Drenagem Linfática"},

    {"id": 4,
      "Nome": "Pedro Oliveira",
        "Telefone": "31 96666-6666",
          "Procedimento": "Massagem Relaxante"}
]


login = input("Por favor, digite seu login: ")
password = input("Por favor digite sua senha: ")


while True:
    check_result = login_check(login, password)

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
        serch_result = search_clients(client_name)
        print(serch_result)



    





   










