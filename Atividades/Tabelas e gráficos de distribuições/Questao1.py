'''
Questão 1):

De acordo com o relatório do IBGE - Estatísticas de Registro Civil 2004 ,
no Brasil, a porcentagem de óbitos violentos para indivíduos do sexo masculino entre 2000 e 2003,
nas Regiões; Norte, Nordeste, Sudeste, Sul e Centro Oeste são: 2000 – Norte 17,4%, Nordeste
13,4%, Sudeste 17,3%, Sul 13,6% e Centro-Oeste 19,6%; 2001 – Norte 17,6%,
Nordeste 13,5%, Sudeste 17,4%, Sul 14,6% e Centro-Oeste 19,4%; 2002 – Norte
17,5%, Nordeste 13,4%, Sudeste 17,5%, Sul 13,5% e Centro-Oeste 19,5%; 2003
– Norte 15,8%, Nordeste 13,6%, Sudeste 17,0%, Sul 13,3% e Centro-Oeste:
19,7%. Organize esses dados em gráficos.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import pandas as pd

anos = [2000, 2001, 2002, 2003]

norte = [17.4, 17.6, 17.5, 15.8]
nordeste = [13.6, 13.5, 13.4, 13.6]
sudeste = [17.3, 17.4, 17.5, 17.0]
sul = [13.6, 14.6, 13.5, 13.3]
centroOeste = [19.6, 19.4, 19.5, 19.7]


regioes = ['Norte', 'Nordeste','Sudeste', 'Sul', 'Centro-Oeste']
#Ano 2000
df_data2000 = [17.4, 13.4, 17.3, 13.6, 19.6]

df2000 = pd.DataFrame(df_data2000)
print(df2000)

#Ano 2001
df_data2001 = [17.6, 13.5, 17.4, 14.6, 19.4]

df2001 = pd.DataFrame(df_data2001)
print(df2001)

#Ano 2002
df_data2002 = [17.5, 13.4, 17.5, 13.5, 19.5]

df2002 = pd.DataFrame(df_data2002)
print(df2002)

#Ano 2003
df_data2003 = [15.8, 13.6, 17.0, 13.3, 19.7]

df2003 = pd.DataFrame(df_data2003)
print(df2003)


fig = plt.figure()
rect = fig.patch
rect.set_facecolor('grey')

#Eixo 1

eixo1 = fig.add_subplot(1, 2, 1, facecolor='w')
eixo1.plot(regioes, df2000, linestyle='-', color='r', marker='s', linewidth=3.0, label='2000')
eixo1.plot(regioes, df2001, linestyle='--', color='g', marker='s', linewidth=3.0, label='2001')
eixo1.plot(regioes, df2002, linestyle=':', color='b', marker='s', linewidth=3.0, label='2002')
eixo1.plot(regioes, df2003, linestyle='-.', color='y', marker='s', linewidth=3.0, label='2003')

eixo1.tick_params(axis='x', colors='c')
eixo1.tick_params(axis='y', colors='c')

eixo1.xaxis.label.set_color('w')
eixo1.yaxis.label.set_color('w')
'''
eixo1.spines['bottom'].set_color('w')
eixo1.spines['top'].set_color('w')
eixo1.spines['left'].set_color('w')
eixo1.spines['right'].set_color('w')
'''

eixo1.legend(loc='upper right')
#plt.axis([0,50,0,100])
eixo1.set_title('Óbitos violentos do sexo masculino entre os anos de 2000 e 2003', color='r')
eixo1.set_xlabel("Regiões")
eixo1.set_ylabel("Porcentagem")

#Eixo 2

eixo2 = fig.add_subplot(1, 2, 2, facecolor='w')
eixo2.plot(anos, norte, linestyle='-', color='r', marker='s', linewidth=3.0, label='Norte')
eixo2.plot(anos, nordeste, linestyle='--', color='g', marker='s', linewidth=3.0, label='Nordeste')
eixo2.plot(anos, sudeste, linestyle=':', color='b', marker='s', linewidth=3.0, label='Sudeste')
eixo2.plot(anos, sul, linestyle='-.', color='pink', marker='s', linewidth=3.0, label='Sul')
eixo2.plot(anos, centroOeste, linestyle='-.', color='y', marker='s', linewidth=3.0, label='Centro Oeste')

eixo2.tick_params(axis='x', colors='c')
eixo2.tick_params(axis='y', colors='c')

eixo2.xaxis.label.set_color('w')
eixo2.yaxis.label.set_color('w')
'''
eixo2.spines['bottom'].set_color('w')
eixo2.spines['top'].set_color('w')
eixo2.spines['left'].set_color('w')
eixo2.spines['right'].set_color('w')
'''

eixo2.legend(loc='upper right')
#plt.axis([0,50,0,100])
eixo2.set_title('Óbitos violentos do sexo masculino entre os anos de 2000 e 2003', color='r')
eixo2.set_xlabel("Anos")
eixo2.set_ylabel("Porcentagem")


plt.show()
