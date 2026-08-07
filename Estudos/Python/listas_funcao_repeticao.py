# 1. Nossa função (a máquina que valida e ajusta o valor)
def processar_valor(escolha):
    valor = float(input(f"Digite o valor para {escolha}: R$ "))
    
    while valor <= 0:
        print("Valor inválido! Digite um valor maior que zero.")
        valor = float(input(f"Digite o valor para {escolha}: R$ "))
    
    if escolha == "saque":
        valor = -valor
        
    return valor

# 2. Estrutura de dados do sistema
historico = []

# 3. Loop principal do aplicativo
while True:
    print("\n--- MENU DO BANCO ---")
    opcao = input("O que deseja fazer? (deposito / saque / sair): ").lower()
    
    if opcao == "sair":
        print("Encerrando o sistema...")
        break
        
    if opcao == "deposito" or opcao == "saque":
        # A MÁGICA ACONTECE AQUI:
        # Chamamos a função e o 'return' dela é guardado diretamente na variável 'valor_final'
        valor_final = processar_valor(opcao)
        
        # Adicionamos ao histórico
        historico.append(valor_final)
        
        # O saldo é a soma de tudo o que está no histórico
        saldo = sum(historico)
        
        print(f"\nTransação realizada! Saldo atual: R$ {saldo:.2f}")
        print(f"Histórico de movimentações: {historico}")
    else:
        print("Opção inválida! Escolha 'deposito', 'saque' ou 'sair'.")