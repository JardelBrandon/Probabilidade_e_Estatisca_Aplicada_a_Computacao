# correlacao entre total geral de Editoracao e de Eventos
import pandas as pd
import matplotlib.pyplot as plt

localDataEditoracao = '/home/arthur/Documents/IFPB/Estatistica/projetos/Dados/Editoracao_newDoc.csv'
localDataEventos = '/home/arthur/Documents/IFPB/Estatistica/projetos/Dados/Eventos_newDoc.csv'

df_editoracao = pd.read_csv(localDataEditoracao, encoding='utf-8', sep=';')
df_eventos = pd.read_csv(localDataEventos, sep=';')

total_editoracao = df_editoracao['Total Geral (R$)']

print(df_editoracao.count())
print("\n-------------------------------------------------------------\n")
print(df_eventos.count())


