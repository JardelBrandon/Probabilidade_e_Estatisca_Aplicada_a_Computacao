'''
Questão 5):

Os depósitos bancários da Empresa AKI-SE-TRABALHA, em milhares de Reais,

    Fev/Mar, 2005:
        3,7     1,6     2,5     3,0     3,9     1,9     3,8     1,5     1,1
        1,8     1,4     2,7     2,1     3,3     3,2     2,3     2,3     2,4
        0,8     3,1     1,8     1,0     2,0     2,0     2,9     3,2     1,9
        1,6     2,9     2,0     1,0     2,7     3,0     1,3     1,5     4,2     
        2,4     2,1     1,3     2,7     2,1     2,8     1,9                 
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dados = [3.7,     1.6,     2.5,     3.0,     3.9,     1.9,     3.8,     1.5,     1.1,
         1.8,     1.4,     2.7,     2.1,     3.3,     3.2,     2.3,     2.3,     2.4,
         0.8,     3.1,     1.8,     1.0,     2.0,     2.0,     2.9,     3.2,     1.9,
         1.6,     2.9,     2.0,     1.0,     2.7,     3.0,     1.3,     1.5,     4.2,
         2.4,     2.1,     1.3,     2.7,     2.1,     2.8,     1.9]

histogram_example = plt.hist(dados, bins=15)

def imprimirTabelaDeFrequencias(baseDeDados):
    count, division = np.histogram(baseDeDados)
    frequenciaAcumulada = 0
    print("\t\t\t\t\t\t\t\t\t\tFrequências")
    print("Classes:\t\t\t\tAbsoluta:\t\tRelativa:\t\tAcumulada:")
    for indice in range(0, len(division)):
        if indice + 1 == len(division):
            break;
        if indice + 2== len(division):
            print('[', "{0:.2f}".format(division[indice]), '|--|',
                  "{0:.2f}".format(division[indice + 1]), ']', end='\t\t\t')
        else:
            print('[', "{0:.2f}".format(division[indice]), '|-- ',
                  "{0:.2f}".format(division[indice + 1]), ')', end='\t\t\t')
        print(count[indice], end='\t\t\t  ')
        print("{0:.2f}".format((count[indice]/sum(count))*100), end='\t\t\t\t')
        frequenciaAcumulada += count[indice]
        print(frequenciaAcumulada)

imprimirTabelaDeFrequencias(dados)
plt.ylabel("Número de frequências ")
plt.xlabel("Classes")
plt.title("Tabela de frequência dos depósitos bancários da Empresa AKI-SE-TRABALHA, em milhares de reais!")
plt.show()