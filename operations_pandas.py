import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4], 'col2': [444,555,666,444], 'col3': ['abc', 'def', 'ghi', 'xyz']})
df.head()

df.info() #expoe classe das variaveis

df.memory_usage() #expoe uso de memoria por cada reparticao do DF

df['col2'].unique() #expoe, de forma unica, todos os elementos do DF

df['col2'].nunique() #informa quantos termos, contados de forma unica, ha na reparticao do DF informado

df['col2'].value_counts() #informa os valores unicos e quantas aparicoes cada um tem na reparticao do DF informado

def comp(x): #definindo func pra aplicar no DF
    return x **2 + 3

df['col1_calc'] = df['col1'].apply(comp) #aplicando func no DF
df

df['col1'].apply(lambda x: x ** 2 + 3) #operacao no df usando func lambda

df['col1'].sum() #soma de coluna

df[df['col2'] == 444] #teste de filtragem de conteudo do DF

df[df['col2']==444] ['col1'].sum() #aplicando operacao em uma filtragem de conteudo do DF

df[df['col2'] == 444]['col1'].apply(lambda x: x * 2)

df.sort_values(by='col2') #aplica funcao sort (organiza) na coluna indicada
df.sort_values(by='col1')

#-=-=-=-=-=-=-=-=-=-=-=-=-=--=--=-=-=-=-=-=-=-=-=

data = {'A': 'foo foo foo bar bar bar'.split(),
        'B': 'one one two two one one'.split(),
        'C': 'x y x y x y'.split(),
        'D': [1,3,2,5,4,1]}

dataf = pd.DataFrame(data)
dataf['E'] = dataf['B'].apply(lambda x: 1 if x == 'one' else 2 )
dataf

dataf.drop('E', axis=1, inplace=True)
dataf

# funcao MAP para DF
dict_map = {'one': '1', 'two': '2'}
dataf['E'] = dataf['B'].map(dict_map)
dataf


dataf.pivot_table(index='A', columns='B', values='D')  #cria uma tabela pivotada, para quando precisamos reorganizar os dados em funcao de alguma coisa
