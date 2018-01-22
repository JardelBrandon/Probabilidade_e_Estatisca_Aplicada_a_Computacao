import pandas as pd
import matplotlib.pyplot as plt

bolsas_no_exterior = pd.read_csv('bolsa-exterior.csv', sep=';')
table = pd.crosstab(index=bolsas_no_exterior['Ano Fase'], columns='Count')
anos = table.index

total_de_bolsas_por_ano = []
for x in range(2006, 2016):
    total_de_bolsas_por_ano.append(bolsas_no_exterior[bolsas_no_exterior['Ano Fase'] == x]['Qtd Bolsas'].sum())

df_data = {'anos': anos, 'bolsas': total_de_bolsas_por_ano}
df = pd.DataFrame(df_data)
print(df)

plt.title('Bolsas por Ano ofertadas no exterior')
plt.bar(anos, total_de_bolsas_por_ano)
plt.show()
'''
print(bolsas_no_exterior[bolsas_no_exterior['Ano Fase'] == 2015]['Qtd Bolsas'])
anos_bolsas = pd.crosstab(index=bolsas_no_exterior['Ano Fase'], columns=bolsas_no_exterior['Qtd Bolsas'].sum())
#print(anos_bolsas)
'''