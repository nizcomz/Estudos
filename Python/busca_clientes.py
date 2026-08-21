def login_check(login, password):
      if login == "admin" and password == "1234":
          print("Acesso Permitido !")
          return True
          
      else:
          print("Acesso negado !"
          "\nTente novamente !")

          return False
            
def search_clients(name):
    while True:
      name = input("Digite o nome do cliente que deseja consultar: ")
      for register in clients:
          if register == name:
                final_register = f"\nNome: {register["nome"]}" f"\nTelefone: {register["nome"]}" f"\nProcedimento: {register["procedimento"]}"
                return final_register
          break
      
      else:
        print("\nCliente não Encontrado !"
             "\nPor favor tente denovo !")
              
      return None
         
clients = [
    {"id": 1,
      "nome": "Maria Silva",
      "telefone": "31 99999-9999",
        "procedimento": "Limpeza de pele"},

    {"id": 2,
      "nome": "João Santos",
        "telefone": "31 98888-8888",
          "procedimento": "Microagulhamento"},

    {"id": 3,
      "nome": "Ana Costa",
        "telefone": "31 97777-7777",
          "procedimento": "Drenagem Linfática"},

    {"id": 4,
      "nome": "Pedro Oliveira",
        "telefone": "31 96666-6666",
          "procedimento": "Massagem Relaxante"}
]

while True:

  login = input("Por favor, digite seu login: ")
  password = input("Por favor digite sua senha: ")

  check_result = login_check(login, password)
      
  if check_result:
    choice = input("\n" \
                    "\nBem vindo ao BD Clinica"
                    "\nEscolha uma opção de consulta"
                    "\n(1) Consultar procedimentos disponíveis" 
                    "\n(2) Consultar Cadastros"
                    "\n(3) Sair"
                    "\n"
                    "\n- ")

    if choice == "3":
        print("\nBanco de dados encerrado !")
        break

    if choice == "2":
        if search_clients:
         print("")


    elif choice == "1":
        for cliente in clients:
          print(f"Procedimentos Disponiveis : {cliente['Procedimento']}")

    else:
        print("Opção inválida")



    





   










