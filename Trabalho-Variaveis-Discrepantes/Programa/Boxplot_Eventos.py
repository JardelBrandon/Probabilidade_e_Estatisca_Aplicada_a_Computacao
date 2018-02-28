import pandas as pd
import matplotlib.pyplot as plt

#------------------------------------------------------------------------------
lista = pd.read_csv('Eventos_edit.csv', sep=';')

filtroPB = pd.DataFrame(lista[lista.UF_Instituição_Benef=="PB"]) 
filtroPB_2015 = pd.DataFrame(filtroPB[filtroPB.Ano_Fase==2015])  

print(filtroPB)

count_prop = filtroPB_2015.groupby(['Instituição_Beneficiária','Qtd_Propostas']).count()
count_prop = count_prop.fillna(0)
total_prop = count_prop.sum(level=0)

print(total_prop)


#------------------------------------------------------------------------------
plt.title('Quantidade de propostas das Instituições na PB (2015)')
total_prop.boxplot('Total_Geral')

p = plt.gca()
p.set_ylim([0,30])


# Boxplot da quantidade de propostas das instituições de ensino na PB
#no ano de 2015