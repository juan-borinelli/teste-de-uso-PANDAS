import pandas as pd
import numpy as np
from numpy.random import randn

outside = 'G1 G1 G1 G2 G2 G2'.split()
inside = [1,2,3, 1,2,3]


#criação de dataframes multi index
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
hier_index
df = pd.DataFrame(np.random.randn(6,2), index=hier_index, columns=['A', 'B'])
df
df.loc['G1']
df.loc['G1'].loc[1]

#realiza troca dos nomes dos index
df.index.names = ['Grupo', 'Numero']
df

#permite fazer cortes semelhantes ao LOC, mas permitindo que seja acessado o 2 index desde que seja especificado (pelo nome). especifica-se a linha, com nuemro, e o index, com nome)
df.xs(1, level='Numero')
