from pandas import*

train_dataset = read_csv("train.csv")

#Lê categórias
#print(train_dataset['age'])
#print(train_dataset['sex', 'age', Fare])
#print(train_dataset.sex)
#print(train_dataset.ix[2 : 10])

#Head lê as 5 primeiras linhas
#print(train_dataset.head())
#print(train_dataset.head(7))

#Tail lê as 5 últimas linhas
#print(train_dataset.tail())
#print(train_dataset.tail(7))

#Outras informações
print(train_dataset.columns) #Imprimir colunas
