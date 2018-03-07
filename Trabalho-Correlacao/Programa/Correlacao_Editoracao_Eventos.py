import pandas as pd
import matplotlib.pyplot as plt

#importando DataFrames
df_editoracao = pd.read_csv('Editoracao.csv', encoding='utf-8', sep=';')
df_eventos = pd.read_csv('Eventos.csv', encoding='utf-8', sep=';')


#Removendo NaN
df_editoracao = df_editoracao.dropna()
df_eventos = df_eventos.dropna()

#Criando listas com as colunas a serem trabalhadas
Editoracao_total_geral = list(df_editoracao['Total Geral (R$)'])
Editoracao_UF = list(df_editoracao['UF Inst Benef Macro'])

Eventos_total_geral = list(df_eventos['Total Geral (R$)'])
Eventos_UF = list(df_eventos['UF Inst Benef Macro'])

#-------------------------------------------------------------------
# Calculando soma de dinheiro investido por estado
#estados em ordem alfabetica (Exemplo:estados[4]=BA)
# 1.AC  2.Al  3.AP  4.AM  5.BA  6.CE  7.DF  8.ES  9.GO 10.MA
#11.MT 12.MS 13.MG 14.PA 15.PB 16.PR 17.PE 18.PI 19.RN 20.RS
#21.RJ 22.RO 23.RR 24.SC 25.SP 26.SE 27.TO
estados = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA',
	'MT','MS','MG','PA','PB','PR','PE','PI','RN','RS',
	'RJ','RO','RR','SC','SP','SE','TO']
#-------------------------------------------------------------------
#Editoracao
cont = 0
Editoracao_somaEstados = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

while (cont < len(Editoracao_UF)):
	isNI = 1 #verifica se o estado foi informado ou  nao informado(NI)
	for i in range(27):
		if (Editoracao_UF[cont] == estados[i]):
			Editoracao_somaEstados[i] += Editoracao_total_geral[cont]
	cont+=1

#-------------------------------------------------------------------
#Eventos
cont = 0
Eventos_somaEstados = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

while (cont < len(Eventos_UF)):
	isNI = 1 #verifica se o estado foi informado ou  nao informado(NI)
	for i in range(27):
		if (Eventos_UF[cont] == estados[i]):
			Eventos_somaEstados[i] += float(Eventos_total_geral[cont])
	cont+=1

#-------------------------------------------------------------------
#-------------------------------------------------------------------
#Criando DataFrame com soma de dinheiro investido por estado 
#em eventos e em editoração
dicionario = {'Eventos (R$)': Eventos_somaEstados, 
	'Editoracao (R$)': Editoracao_somaEstados, 'UF': estados}

new_df = pd.DataFrame(dicionario)


print(new_df)

#imprime a correlacao entre os dados do DataFrame
print(new_df.corr())

scatter_plot = plt.scatter(new_df['Eventos (R$)'], new_df['Editoracao (R$)'], alpha=0.5, c=new_df['Editoracao (R$)'])
plt.title('Dinheiro investido por estado')
plt.ylabel('Gastos com editoração')
plt.xlabel('Gastos com eventos')
plt.show()



