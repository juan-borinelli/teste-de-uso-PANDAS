import pandas as pd

#criar 2 dfs com os arquivos da pasta gasolina e juntar os 2 dfs em 1 so
df2000 = pd.read_csv('gasolina/gasolina_2000+.csv', index_col='Unnamed: 0')
df2000

df2010 = pd.read_csv('gasolina/gasolina_2010+.csv', index_col='Unnamed: 0')
df2010

df_geral = pd.concat([df2000, df2010])
df_geral

df_geral.info()
df_geral.head()

# exibir a terceira chamada da coluna 'DATA INICIAL'
df_geral[['DATA INICIAL']].iloc[2]

# transformar as colunas de data em type datetime
df_geral['DATA INICIAL'] = pd.to_datetime(df_geral['DATA INICIAL'])
df_geral['DATA FINAL'] = pd.to_datetime(df_geral['DATA FINAL'])

df_geral.info()

# criar nova coluna contendo somente mes e ano a partir da coluna 'DATA FINAL'
df_geral['MES E ANO'] = df_geral['DATA FINAL'].dt.strftime('%m/%Y')


#utilize value counts para visualizar todos os tipo de produtos contidos na base de dados
df_geral['PRODUTO'].value_counts()

# filtre o df para obter somente resultados referentes a 'GASOLINA COMUM' e grave em uma nova variavel
df_gasol_comum = df_geral[df_geral['PRODUTO'] == 'GASOLINA COMUM']
df_gasol_comum

# preco media de revenda da gasolina comum em agosto de 2008
med_ago_2008_gas = df_gasol_comum[df_gasol_comum['MES E ANO'] == '08/2008']['PREÇO MÉDIO REVENDA'].mean()

# preco medio de revenda em maio de 2014 em SAO PAULO
med_maio_2014_sp_gas = df_gasol_comum[df_gasol_comum['MES E ANO'] == '05/2014'][df_gasol_comum['ESTADO'] == 'SAO PAULO']['PREÇO MÉDIO REVENDA'].mean()

# estados em que a gasolina ultrapassou 5,00
df_gasol_comum[df_gasol_comum['PREÇO MÉDIO REVENDA'] > 5]['ESTADO'].value_counts()
# quando ocorreu
df_gasol_comum[df_gasol_comum['PREÇO MÉDIO REVENDA'] > 5]['MES E ANO'].value_counts()

# media de preco dos estados da regiao sul em 2012
df_gasol_comum['ANO'] = df_gasol_comum['DATA FINAL'].dt.strftime('%Y')
df_gasol_comum[df_gasol_comum['ANO'] == '2012'][df_gasol_comum['REGIÃO'] == 'SUL']['PREÇO MÉDIO REVENDA'].mean()
