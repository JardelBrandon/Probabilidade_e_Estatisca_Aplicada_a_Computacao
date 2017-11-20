'''
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

import pandas as pd

#'anos': [2000, 2001, 2002, 2003],
#Ano 2000
df_data2000 = {'Porcentagem': [17.4, 13.4, 17.3, 13.6, 19.6]}

df2000 = pd.DataFrame(df_data2000)
print(df2000)

#Ano 2001
df_data2001 = {'Porcentagem': [17.6, 13.5, 17.4, 14.6, 19.4]}

df2001 = pd.DataFrame(df_data2001)
print(df2001)

#Ano 2002
df_data2002 = {'Regioes': ['Norte', 'Nordeste','Sudeste', 'Sul', 'Centro-Oeste'],
            'Porcentagem': [17.5, 13.4, 17.5, 13.5, 19.5]}

df2002 = pd.DataFrame(df_data2002)
print(df2002)

#Ano 2003
df_data2003 = {'Regioes': ['Norte', 'Nordeste','Sudeste', 'Sul', 'Centro-Oeste'],
            'Porcentagem': [15.8, 13.6, 17.0, 13.3, 19.7]}

df2003 = pd.DataFrame(df_data2003)
print(df2003)


pie_2000 = ['Norte', 'Nordeste','Sudeste', 'Sul', 'Centro-Oeste']
#pie_2001 = df2001.loc['Regioes']
#pie_2002 = df2002.loc['Regioes']
#pie_2003 = df2003.loc['Regioes']

fig, eixos = plt.subplots(nrows=1, ncols=2, figsize=(8,4))

pie_1 = eixos[0].pie(pie_2000, labels=['Norte', 'Nordeste','Sudeste', 'Sul', 'Centro-Oeste'],
                                            autopct='%1.1f%%', colors=['gold', 'lightskyblue'])

eixos[0].set_title('Óbitos violentos do sexo masculino no ano: 2000')
eixos[0].axis('equal')
