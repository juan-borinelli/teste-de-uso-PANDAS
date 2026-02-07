import pandas as pd
import datetime

#definindo tempo de analise do nosso DF
numero_de_dias = 100
datas = pd.date_range(start='1/1/2021', periods=numero_de_dias)
datas

#associando o tempo de analise ao DF
df = pd.DataFrame(range(numero_de_dias), columns=['number'], index=datas)
df

df.index #datatime index (contem informacoes do tipo datetime, direto atraves do pandas)

df.index[0].day 
df.index[0].year
df.index[0].month

df[df.index.month == 4] #filtra para conteudo somente do mes 4
df[df.index.day ==  10]

df['Month'] = df.index.month
df

df[df.index > datetime.datetime(2021, 1, 10)]