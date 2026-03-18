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
df_gas['MES E ANO'] = df_gas['DATA FINAL'].dt.strftime('%Y/%m')

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
df_gas_comum[df_gas_comum['PREÇO MÉDIO REVENDA'] > 5][['ESTADO', 'MES', 'ANO', 'PREÇO MÉDIO REVENDA']]
df_gas_comum['MES E ANO'] = df_gas_comum['MES'] + '/' + df_gas_comum['ANO']
df_gas_comum[df_gas_comum['PREÇO MÉDIO REVENDA'] > 5]['MES E ANO'].value_counts()

# media de preco dos estados da regiao sul em 2012
df_teste = df_gas_comum[df_gas_comum['DATA FINAL'].apply(lambda x: x.year)==2012]
df_teste[df_teste['REGIÃO']=='SUL']['PREÇO MÉDIO REVENDA'].mean()
df_gas_comum[df_gas_comum['REGIÃO']=='SUL'][df_gas_comum['ANO']=='2012']['PREÇO MÉDIO REVENDA']

# tabela com a variacao percentual ano a ano do preco da gasolina no estado do RJ
dic_ano = df_gas_comum[df_gas_comum['ESTADO']=='RIO DE JANEIRO']['ANO'].value_counts().index

final_medias = []
anos = []
for ano in dic_ano.sort_values():
    current_media = df_gas_comum[df_gas_comum['ESTADO']=='RIO DE JANEIRO'][df_gas_comum['ANO']==ano]['PREÇO MÉDIO REVENDA'].mean()
    final_medias.append(current_media)
    anos.append(ano)
    #problema encontrado aqui: na lista final_medias o ultimo resultado esta repetindo e sendo jogado para o inicio da lista
len(final_medias)
len(anos)
df_varia = pd.DataFrame({'ANO': anos, 'VARIACAO': final_medias})
df_varia['VARIACAO'] = (df_varia['VARIACAO'] / df_varia['VARIACAO'].shift(1) - 1) * 100

# tabela temporal contendo diferença absoluta e percentual entre os valores mais baratos e mais caros, apresente também os respectivos estados dos preços
df_min = df_gas_comum.groupby('MES E ANO')['PREÇO MÉDIO REVENDA'].min()
df_max = df_gas_comum.groupby('MES E ANO')['PREÇO MÉDIO REVENDA'].max()
df_dif = pd.DataFrame()
df_dif['abs_diff'] = df_max - df_min
df_dif['percent_diff'] = (df_dif['abs_diff']) / df_min * 100
df_dif['max'] = df_max
df_dif['min'] = df_min
df_dif
idx_max = df_gas_comum.groupby('MES E ANO')['PREÇO MÉDIO REVENDA'].idxmax()
idx_min = df_gas_comum.groupby('MES E ANO')['PREÇO MÉDIO REVENDA'].idxmin()
df_dif['ESTADO_MAX'] = df_gas_comum.loc[idx_max]['ESTADO'].values
df_dif['ESTADO_MIN'] = df_gas_comum.loc[idx_min]['ESTADO'].values
#usado values no final pq essa tabela n é igual a tabela de origem dos dados de idx (index nao correspondem), porém são de mesmo tamanho e abrigarão dados da tabela de origem
df_dif['ESTADO_MAX'].value_counts()