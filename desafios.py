import pandas as pd

#criando df para os dois levantamentos de preco
df_gasolina = pd.read_csv('gasolina/gasolina_2000+.csv', index_col=0)
df_gasol = pd.read_csv('gasolina/gasolina_2010+.csv', index_col=0)

#juntando os dois levantamentos
df_gas = pd.concat([df_gasolina, df_gasol])
df_gas

df_gasol.head()

df_gas['DATA INICIAL'].iloc[2]
df_gas['DATA INICIAL'] = pd.to_datetime(df_gas['DATA INICIAL'])
df_gas['DATA FINAL'] = pd.to_datetime(df_gas['DATA FINAL'])
df_gas['DATA INICIAL'].info()
df_gas['DATA FINAL'].info()
df_gas.info()

# criar coluna de mes e ano

df_gas['MES'] = df_gas['DATA FINAL'].dt.strftime('%m')
df_gas['ANO'] = df_gas['DATA FINAL'].dt.strftime('%Y')

#usando value_counts para listar todos os tipos de produtos contidos na base de dados
df_gas['PRODUTO'].value_counts()

#gravar em uma nova variavel um df com dados somente de 'GASOLINA COMUM'
df_gas_comum = df_gas[df_gas['PRODUTO']=='GASOLINA COMUM']
df_gas_comum

# media do preco de revenda da gasolina em agosto de 2008
df_gas_comum[df_gas_comum['MES']=='08'][df_gas_comum['ANO']=='2008']['PREÇO MÉDIO REVENDA'].mean()

# media de preco de revenda em SP em maio de 2014
df_gas_comum[df_gas_comum['MES']=='05'][df_gas_comum['ANO']=='2014'][df_gas_comum['ESTADO']=='SAO PAULO']['PREÇO MÉDIO REVENDA'].mean()

# quais estados a gasosa passou dos 5 pila, e quando foi
df_gas_comum[df_gas_comum['PREÇO MÉDIO REVENDA'] > 5]['ESTADO'].value_counts()
df_gas_comum['MES E ANO'] = df_gas_comum['MES'] + '/' + df_gas_comum['ANO']
df_gas_comum[df_gas_comum['PREÇO MÉDIO REVENDA'] > 5]['MES E ANO'].value_counts()

# media de preco dos estados da regiao sul em 2012
df_gas_comum[df_gas_comum['REGIÃO']=='SUL'][df_gas_comum['ANO']=='2012']['PREÇO MÉDIO REVENDA'].mean()

# tabela com a variacao percentual ano a ano do preco da gasolina no estado do RJ
todos_anos = df_gas_comum[df_gas_comum['ESTADO']=='RIO DE JANEIRO']['ANO'].value_counts().to_dict()
todos_anos
lista_de_anos = []
for ano, quant in todos_anos.items():
    lista_de_anos.append(ano)
lista_de_anos.sort()

lista_medias = []
for data in lista_de_anos:
    media_anual_gas_comum = df_gas_comum[df_gas_comum['ESTADO']=='RIO DE JANEIRO']['ANO']
    media_anual_gas_comum
    lista_medias.append(media_anual_gas_comum)
lista_medias