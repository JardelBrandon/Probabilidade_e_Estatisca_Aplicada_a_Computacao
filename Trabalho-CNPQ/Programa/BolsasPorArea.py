import pandas as pd
import matplotlib.pyplot as plt

bolsas_no_exterior = pd.read_csv('2015.csv', sep=';')
table = pd.crosstab(index=bolsas_no_exterior['Grande Área'], columns='Count')
print(table)
print(table.columns)
print(table.index)


plt.title('Grandes áreas de pesquisa no ano 2015')
plt.barh(table.index, table['Count'], align='center')
plt.ylabel('Áreas')
plt.xlabel('Quantidade')
plt.show()
