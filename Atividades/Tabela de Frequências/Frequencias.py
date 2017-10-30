import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from numpy.random import normal,rand

'''
os.chdir('C:\\Users\ifpb\Documents\GitHub\Probabilidade_e_Estatisca_Aplicada_a_Computacao\Atividades\Tabela de Frequências') # Set working directory
train = pd.read_csv("train.csv") # Read the data
char_cabin = train["cabin"].astype(str) # Convert cabin to str
new_Cabin = np.array([cabin[0] for cabin in char_cabin]) # Take first letter
train["cabin"] = pd.Categorical(new_Cabin) # Save the new cabin var
'''

#a) Tabela de frequências para survived
train = pd.read_csv("train.csv")
my_tab = pd.crosstab(index=train["survived"],  columns="count") # Name the count column# Make a crosstab
print(my_tab)


#b) Tabela de frequências para age
train = pd.read_csv("train.csv")
my_tab = pd.crosstab(index=train["age"],  columns="count") # Name the count column# Make a crosstab
print(my_tab)


#c) Tabela de frequências para embarked
train = pd.read_csv("train.csv")
my_tab = pd.crosstab(index=train["embarked"],  columns="count") # Name the count column# Make a crosstab
print(my_tab)

print(type(my_tab)) # Confirm that the crosstab is a DataFrame

train['survived'].fillna(train['survived'].mean(), inplace=True)
histogram_example = plt.hist(train['survived'], bins=15)
plt.show()

'''
train['embarked'].fillna(train['embarked'].mean(), inplace=True)
histogram_example = plt.hist(train['embarked'], bins=15)
plt.show()
'''

train['age'].fillna(train['age'].mean(), inplace=True)
histogram_example = plt.hist(train['age'], bins=15)
plt.show()

