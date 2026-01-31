import pandas as pd
import numpy as np

df = pd.DataFrame({
'A': [1,2, np.nan],
'B': [5, np.nan, np.nan],
'C': [1,2,3]
})

df

df.dropna() #sem axis definido elimina as linhas
df.dropna(axis=1) #com axis =1 elimina colunas

df.dropna(axis=1, thresh=2) #thresh se refere ao liimite de numeros para decisao de descarte da linha ou coluna
#thresh = 2 (sempre que for encontrado 2 ou mais valores ausentes, serao descartados)
#util para filtrar um conjunto de dados em que sem alguma informacao valiosa ficaria inviavel de trabalhar

df.fillna("aqui") #sempre que encontrar valores nan, trocara pelo valor solicitado no parenteses
#usado para nao atrapalhar operacoes futuras

df['A'].mean() #calculo para media de 'A'

df['A'].fillna(value=df['A'].mean()) #preenchimento de NANs com media para nao prejudicar a distribuicao amostral

df.ffill() #realiza preenchimento com base nas amostragens passadas, preenchendo com o ultimo valor observavel
#ideal para series em que o indice se trata de tempo
