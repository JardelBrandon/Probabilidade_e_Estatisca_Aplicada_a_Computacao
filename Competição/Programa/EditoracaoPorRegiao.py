import pandas as pd
import matplotlib.pyplot as plt


editoracao = pd.read_csv('Editoracao.csv', encoding='utf-8', sep=';')

regioes_editoracao = pd.crosstab(index=editoracao['Região Inst Benef Macro'], columns="count")
fig, eixos = plt.subplots(nrows=1, ncols=1, figsize=(8,4))

pie_1 = eixos.pie(regioes_editoracao, labels=regioes_editoracao.index, autopct='%1.1f%%', colors=['gold', 'lightskyblue', 'red', 'pink', 'green'])

eixos.set_title('Regiões mais beneficiadas')
eixos.axis('equal')

plt.show()


