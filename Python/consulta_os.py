import os  # Chamas o assistente que sabe mexer no computador

# 1. Você diz QUAL pasta ele deve olhar
pasta = r"C:\Users\lenovo\Documents"

# 2. O comando listdir() vai lá dentro, pega TUDO e guarda numa lista
conteudo = os.listdir(pasta)

# 3. O 'for' passa olhando item por item que ele encontrou
for item in conteudo:
    print(item)


