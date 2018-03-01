import pandas as pd
import matplotlib.pyplot as plt

apoio_editoracao = pd.read_csv('Eventos.csv', sep=';')
coluna_total_geral = apoio_editoracao["Total Geral (R$)"]

print("********************************************************")
print("Valores dos Quartis: \n")
print("Valor do primeiro quartil:")
print(coluna_total_geral.quantile(0.25), "\n")
print("Valor do segundo quartil (mediana):")
print(coluna_total_geral.quantile(), "\n")
print("Valor do terceiro quartil:")
print(coluna_total_geral.quantile(0.75))
print("********************************************************")

valor_condicao = 500000

coluna_total_geral_menor_valores = coluna_total_geral[coluna_total_geral < valor_condicao]
coluna_total_geral_maior_valores = coluna_total_geral[coluna_total_geral > valor_condicao]

fig, (ax1, ax2) = plt.subplots(figsize=(8, 3), ncols=2)
fig.suptitle("Valores totais das bolsas de apoio a Eventos", size=20)

ax1.hist(coluna_total_geral_menor_valores)
ax1.set_title("Valores totais menores que R$:500.000", size=15)
ax1.set_xlabel("Valores", size=10)
ax1.set_ylabel("Frequência", size=10)

ax2.hist(coluna_total_geral_maior_valores)
ax2.set_title("Valores totais maiores que R$:500.000", size=15)
ax2.set_xlabel("Valores", size=10)
ax2.set_ylabel("Frequência", size=10)

plt.show()

