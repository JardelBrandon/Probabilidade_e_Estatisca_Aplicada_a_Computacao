'''
Questão 4):

Os depósitos bancários de uma empresa, em milhares de reais, são dispostos na tabela abaixo:

        3,7     1,6     2,5     3,0     3,9     1,9     3,8     1,5     1,1
        1,8     1,4     2,7     2,1     3,3     3,2     2,3     2,3     2,4
        0,8     3,1     1,8     1,0     2,0     2,0     2,8     3,2     1,9
        1,6     2,9     2,0     1,0     2,7     3,0     1,3     1,5     4,2
        2,4     2,1     1,3     2,7     2,1     2,8     1,9
        
        
a) Construa a distribuição de frequências dos dados
b) Construa o histograma
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd

dados = [3.7,     1.6,     2.5,     3.0,     3.9,     1.9,     3.8,     1.5,     1.1,
         1.8,     1.4,     2.7,     2.1,     3.3,     3.2,     2.3,     2.3,     2.4,
         0.8,     3.1,     1.8,     1.0,     2.0,     2.0,     2.8,     3.2,     1.9,
         1.6,     2.9,     2.0,     1.0,     2.7,     3.0,     1.3,     1.5,     4.2,
         2.4,     2.1,     1.3,     2.7,     2.1,     2.8,     1.9,]

histogram_example = plt.hist(dados, bins=15)

plt.show()
