import pandas as pd
import numpy as np
from numpy.random import randn

labels = ['a', 'b', 'c']

minha_lista = [10, 20, 30]

arr = np.array([10,20,30])

d = {'a':10, 'b':20, 'c':30}

pd.Series(d)

ser1 = pd.Series([1,2,3,4], index=['EUA', 'GER', 'RUS', 'JPN'])
ser2 = pd.Series([1,2,5,4], index= ['EUA', 'GER', 'ITL', 'JPN'])
ser1 + ser2

df = pd.DataFrame(randn(5, 4), index='A B C D E'.split(), columns='UM DOIS TRES QUATRO'.split())
df['CINCO'] = df['DOIS'] + df['TRES'] #gerando uma nova coluna em df
'''
df.drop('CINCO', axis=1) #excluindo (temporariamente) uma coluna
df.drop('CINCO', axis=1, inplace=True) #parametro inplace define que as mudancas realizadas na linha se tornem permanentes no arquivo orginal

df.loc['A'] #LOCALIZA LINHA DENTRO DO COLCHETES E FAZ TRANSPOSICAO(?) TROCANDO LINHA POR COLUNA QUANDO SOMENTE UMA LINHA FOR CHAMADA NA FUNCAO

df.iloc[0, 2] #funcao para localizar, em formato [x,y], um valor na tabela, prenchendo sua coordenadas dentro do colchetes -> aqui localizará na linha A (0) e na coluna TRES (2)
'''

df
df.loc['A'] #para exibir o que vem na coluna, em formato de coluna transposicionada, chamando pela linha a string pra selecionar coluna
df.loc[['A']] #para exibir o que vem na coluna, no formato original, chamando pela linha a string pra selecionar a coluna
df.loc[['A', 'B'],'DOIS'] #para exibir as linhas selecionadas nos colchetes internos, mas considerando somente as colunas citadas nos colchetes externos
df.loc[['D', 'E'], ['UM', 'TRES']] #linhas 'D' e 'E' nas colunas 'UM' e 'TRES'
df.iloc[:-1, 1:4] #forma de exibição utilizando seleção numérica -> :-1 (todas as linhas menos a ultima), 1:4 (da coluna 1 até a coluna 3)
df.iloc[1:4, 1:3]

#operacoes condicionais

df
df[df > 0] #forma de filtrar dados em um dataframe
df.loc['B'] > 0 #forma de filtrar dados por linha
df['TRES'] > 0 #forma de filtrar dados por coluna
df[df['TRES'] > 0] #forma de filtrar dados semelhantes por coluna (mantem somente as linhas em que os valores da coluna TRES sao maiores que 0)
