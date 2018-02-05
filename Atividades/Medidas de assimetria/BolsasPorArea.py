import pandas as pd
import matplotlib.pyplot as plt
from bokeh.charts import BoxPlot

bolsas_no_exterior = pd.read_csv('2015.csv', sep=';')
table = pd.crosstab(index=bolsas_no_exterior['Grande Área'], columns='Count')
print(table)
print(table.columns)
print(table.index)



box = BoxPlot(train_df, label="Bolsas", values="Fare")
output_file("bokeh_boxplot.html")
show(box)
