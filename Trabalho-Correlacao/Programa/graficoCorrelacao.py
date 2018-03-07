"""
Colocar no relatorio:
1. A correlação dos anos 2006 e 2011 não sõa confiáveis pois há um
   grande número de unidades federativas nao informadas nesses anos
   no DataFrame de Editoração
2. A correlação do ano 2015 é 0 pois nenhuma das unidades federativas
   foi informada nesse ano no DataFrame de Editoração
3. A correlação do ano 2016 é 0 pois não existem dados sobre esse ano
   no DataFrame de Editoração
"""

import pandas as pd
import matplotlib.pyplot as plt


anos = [2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]
correlacao = [0.937955,0.98115,0.982439,0.954704,
		0.979344,0.439523,0.971822,0.966961,
		0.972341,0,0]


plt.title('Investimentos em Eventos e Editoracao*')
plt.bar(anos, correlacao, align='center')
plt.ylabel('correlacao')
plt.xlabel('ano')
plt.show()
