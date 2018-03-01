import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

apoio_editoracao = pd.read_csv('Editoracao.csv', sep=';')
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

print("********************************************************")
print("Valores de assimetria: \n")
print(coluna_total_geral.skew())
print("********************************************************")

print("********************************************************")
print("Valores de curtose: \n")
print(coluna_total_geral.kurt())
print("********************************************************")


valor_condicao = 500000

coluna_total_geral_menor_valores = coluna_total_geral[coluna_total_geral < valor_condicao]
coluna_total_geral_maior_valores = coluna_total_geral[coluna_total_geral > valor_condicao]

fig1, (ax1, ax2) = plt.subplots(ncols=2)
fig1.suptitle("Valores totais das bolsas de apoio a Editoração", size=20)
fig1.set_size_inches(12, 6)

ax1.hist(coluna_total_geral_menor_valores, color="red")
ax1.set_title("Valores totais menores que R$:500.000", size=15)
ax1.set_xlabel("Valores", size=10)
ax1.set_ylabel("Frequência", size=10)

ax2.hist(coluna_total_geral_maior_valores, color="red")
ax2.set_title("Valores totais maiores que R$:500.000", size=15)
ax2.set_xlabel("Valores", size=10)
ax2.set_ylabel("Frequência", size=10)



fig2, ax3 = plt.subplots()
matplotlib.style.use('ggplot')
apoio_editoracao.boxplot(column='Total Geral (R$)')
ax3.set_title("BoxPlot, total geral Editoração")
ax3.set_ylabel("Valores em Reais(R$)")
fig2.set_size_inches(10, 7)

plt.show()