import pandas as pd

tabelas = pd.read_html("https://pt.wikipedia.org/wiki/Lista_de_filmes_de_maior_bilheteria")


tabela = tabelas[0]

print(tabela)

tabela_filtrada = tabela[["Diretor(a)", "Bilheteria (US$)"]]

print(tabela_filtrada)


# Remover espaços e os pontos (separadores de milhar)
tabela_filtrada["Bilheteria (US$)"] = tabela_filtrada["Bilheteria (US$)"].str.replace(r'\.', '', regex=True)
# Remover também os espaços
tabela_filtrada["Bilheteria (US$)"] = tabela_filtrada["Bilheteria (US$)"].str.replace(r'\s+', '', regex=True)
# Agora, converta para inteiro
tabela_filtrada["Bilheteria (US$)"] = tabela_filtrada["Bilheteria (US$)"].astype("int64")


print(tabela_filtrada.groupby("Diretor(a)").sum())