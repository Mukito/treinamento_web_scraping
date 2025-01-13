import pandas as pd

# Extrair os dados da tabela a partir do link da web
tabelas = pd.read_html("https://pt.wikipedia.org/wiki/Lista_de_filmes_de_maior_bilheteria")

# Lista com as tabelas o [0] para pegar a primeira tabela
tabela = tabelas[0]

print(tabela)

# Filtro a tabela com as colunas que quero
tabela_filtrada = tabela[["Diretor(a)", "Bilheteria (US$)"]]

print(tabela_filtrada)

# Trato os meus dados e transformo em valores numericos

# Remover espaços e os pontos (separadores de milhar)
tabela_filtrada["Bilheteria (US$)"] = tabela_filtrada["Bilheteria (US$)"].str.replace(r'\.', '', regex=True)
# Remover também os espaços
tabela_filtrada["Bilheteria (US$)"] = tabela_filtrada["Bilheteria (US$)"].str.replace(r'\s+', '', regex=True)
# Agora, converta para inteiro
tabela_filtrada["Bilheteria (US$)"] = tabela_filtrada["Bilheteria (US$)"].astype("int64")

# Faço o argumento por diretor o .sum no final para somar por diretor
print(tabela_filtrada.groupby("Diretor(a)").sum())
