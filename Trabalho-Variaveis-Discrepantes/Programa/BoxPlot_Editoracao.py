# Boxplot da quantidade de propostas por ano, a nível nacional
import pandas as pd
import matplotlib.pyplot as plt


editoracao = pd.read_csv('Editoracao.csv', encoding='utf-8', sep=';')

editoracao.boxplot(column='Qtd Propostas', by='Ano Fase')
p = plt.gca()
p.set_ylim([0,40])
plt.title('axes title')

plt.show()

# Boxplot da quantidade de propostas por ano, a nível nacional

