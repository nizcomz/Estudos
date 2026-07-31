# def = define uma função. Exemplo: def saudacao(): cria uma função chamada saudacao
# return = retorna um valor de uma função para quem a chamou
# if/elif/else = escolhe qual bloco de código executar conforme uma condição
# while = repete um bloco de código enquanto a condição for verdadeira
# for = percorre cada item de uma coleção, como uma lista

# Define uma função para mostrar o histórico de transações
def historico(historico_transacoes):
    # print() mostra texto na tela
    print("Histórico de transações:")
    # for percorre cada transacao dentro da lista historico_transacoes
    for transacao in historico_transacoes:
        # imprime cada item da lista
        print(transacao)

# Define uma função para verificar se a escolha é saque ou depósito
# escolha = texto digitado pelo usuário
# verificacao_saque = lista com valores válidos para saque
# verificacao_deposito = lista com valores válidos para depósito
def verificacao(escolha, verificacao_saque, verificacao_deposito):
    # if verifica se escolha pertence à lista verificacao_saque
    if escolha in verificacao_saque:
        print("Transação selecionada: SAQUE")
        return "saque"  # retorna uma string indicando o tipo de transação
    # elif = "se não, se": testa outra condição se a primeira for falsa
    elif escolha in verificacao_deposito:
        print("Transação selecionada: DEPÓSITO")
        return "deposito"
    else:
        # else executa quando nenhuma condição anterior for verdadeira
        print("Transação inválida. Por favor, escolha entre 'Saque' ou 'Depósito'.")
        return None

# Cria uma lista vazia para armazenar as transações
# [ ] = cria uma lista vazia
historico_transacoes = []
# Listas de palavras que reconhecem saque e depósito
verificacao_saque = ["saque", "SAQUE", "Saque", "SaQuE"]
verificacao_deposito = ["deposito", "DEPOSITO", "Deposito", "DePoSiTo"]

# Loop principal do programa: repete até o usuário escolher sair
while True:
    print("Menu:")
    print("1. Adicionar transação")
    print("2. Ver histórico de transações")
    print("3. Sair")

    # input() lê texto digitado pelo usuário
    opcao = input("Escolha uma opção: ")

    # Verifica a opção escolhida pelo usuário
    if opcao == "1":
        # .lower() transforma o texto em letras minúsculas
        escolha = input("Qual transação você deseja realizar (Saque/Depósito): ").lower()
        # chama a função verificacao e guarda o resultado em tipo
        tipo = verificacao(escolha, verificacao_saque, verificacao_deposito)

        if tipo == "saque":
            # while True cria um loop que só termina com break
            while True:
                valor_saque = float(input("Qual valor você deseja sacar? "))
                if valor_saque > 0:
                    transacao = -valor_saque  # valor negativo representa saque
                    historico_transacoes.append(transacao)
                    # .append() adiciona o item ao final da lista
                    print("Transação adicionada com sucesso!")
                    break  # encerra o loop do saque
                else:
                    print("Valor inválido para saque. Digite um valor maior que zero.")

        elif tipo == "deposito":
            while True:
                valor_deposito = float(input(f"Qual valor você deseja depositar? "))
                if valor_deposito > 0:
                    transacao = valor_deposito
                    historico_transacoes.append(transacao)
                    print("Transação adicionada com sucesso!")
                    break
                else:
                    print("Valor inválido para depósito. Digite um valor maior que zero.")

        else:
            # Se tipo for None, a escolha não foi válida
            print("Não foi possível adicionar a transação. Tente novamente.")

    elif opcao == "2":
        if len(historico_transacoes) == 0:
            print("Nenhuma transação registrada ainda.")
        else:
            historico(historico_transacoes)

    elif opcao == "3":
        print("Saindo do programa...")
        break  # sai do loop principal e encerra o programa

    else:
        print("Opção inválida. Tente novamente.")
        