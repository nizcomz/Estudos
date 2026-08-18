def validar_senha(senha): # Cria um função com uma variavel vazia
    if len(senha) >= 8 and senha != "12345678":
        return True
    else:
        return False
    
# Começa o loop
while True:
    nova_senha = input("Qual a nova senha ?: ")
# Aqui chamamos a função e colocamos o valor de nova_senha dentro da "caixa" senha
    if validar_senha(nova_senha): 
        print("Senha Válida !")
        break #Encerra o loop
    else:
        print("Senha Inválida")


        

    