import pandas as pd
import matplotlib.pyplot as plt

apoio_editoracao = pd.read_csv('Editoracao.csv', sep=';')

plt.hist(apoio_editoracao['Total Geral (R$)'], bins=15, orientation='horizontal')
plt.title("Valores totais por projetos de editoração")
plt.xlabel("Frequencia")
plt.ylabel("Valor R$")
plt.show()
