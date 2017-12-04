'''
Questão 2):

A distribuição abaixo indica o número de acidentes ocorridos em uma empresa com 70 funcionários. (Dados fictícios).

        Nº de acidentes    | 0   1   2   3   4   5   6   7
        Nº de funcionários |20   10  16  9   6   5   3   1
        
Determine:
    a) O número de funcionários que não sofreram acidente
    b) O número de funcionários que sofreram pelo menos 4 acidentes
    c) O número de funcionários que sofreram 1 < acidentes <= 4
    d) O número de funcionários que sofreram no mínimo 3 e no máximo 5 acidentes 
    e) A porcentagem dos funcionários que sofreram no mínimo 5 acidentes
    f) A porcentagem dos funcionários que sofreram entre 2 e 4 acidentes 
    g) Gráficos de colunas e de barras 
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd


df_data = {'Número de acidentes': [0, 1, 2, 3, 4, 5, 6, 7],
           'Número de funcinários': [20, 10, 16, 9, 6, 5, 3, 1]}

df = pd.DataFrame(df_data)
print(df)

print("a) O número de funcionários que não sofreram acidente: 20")
print("b) O número de funcionários que sofreram pelo menos 4 acidentes: 15")
print("c) O número de funcionários que sofreram 1 < acidentes <= 4: 31")
print("d) O número de funcionários que sofreram no mínimo 3 e no máximo 5 acidentes: 20")
print("e) A porcentagem dos funcionários que sofreram no mínimo 5 acidentes:", ((5+3+1)/100), "%")
print("f) A porcentagem dos funcionários que sofreram entre 2 e 4 acidentes:", ((16+9+6)/100), "%")

#Gráfico de barras e de colunas

y_axis = [20, 10, 16, 9, 6, 5, 3, 1]
x_axis = [0, 1, 2, 3, 4, 5, 6, 7]
width_n = 0.4
bar_color = 'yellow'
plt.bar(x_axis, y_axis, width=width_n, color=bar_color, align='center')
plt.title("Número de funcionários por acidentes na empresa")
plt.ylabel("Número de funcionários ")
plt.xlabel("Número de acidentes")
plt.show()
