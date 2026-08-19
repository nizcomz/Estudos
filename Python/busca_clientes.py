
def buscar_clientes(busca):
    for busca in clientes:
        print("\nID: ", [id]
        "\nNome: ", [nome]
        "\nTelefone: ", [telefone]
        "\nProcedimento: ", [procedimento])
        return True
    else:
        print("Cliente não encontrado")
        return None
        
busca = []

clientes = [
    {"id": 1, "nome": "Maria Silva", "telefone": "31 99999-9999", "procedimento": "Limpeza de pele"},
    {"id": 2, "nome": "João Santos", "telefone": "31 98888-8888", "procedimento": "Microagulhamento"},
    {"id": 3, "nome": "Ana Costa", "telefone": "31 97777-7777", "procedimento": "Drenagem Linfática"},
    {"id": 4, "nome": "Pedro Oliveira", "telefone": "31 96666-6666", "procedimento": "Massagem Relaxante"}
]



while True:
    print("Bem vindo ao BD Clinica")
    client_search = input("Digite o nome do cliente que deseja consultar: ").lower()
    busca.append(client_search)
    buscar_clientes





    










