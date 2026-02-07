import pandas as pd

data = {
    'Classe': 'Junior Junior Pleno Pleno Senior Senior'.split(),
    'Nome': 'Jorge Carlos Roberta Patricia Bruno Vera'.split(),
    'Venda': [200,120,340,124,243,350]
}

df = pd.DataFrame(data)
df

#agrupamento de informacoes 
#qual foi a media de venda das classes de vendedores
classe = df.groupby('Classe')
classe.mean(numeric_only=True) #media
classe.sum(numeric_only=True) #soma

df.groupby('Classe').sum(numeric_only=True) #forma mais direta de realizar operacoes, sem variavel definida

df.groupby('Classe').max() #em operacoes de min e max é possível usar com e sem numeric_only. Sem nmc aparece os nome, com nmc somente numeros e coluna definida ('classe' nesse caso)
df.groupby('Classe').min(numeric_only=True)

df2 = df.copy()
df2['Venda'] = [150,432,190,230,410,155]
df2
df3 = pd.concat([df, df2])
df3
df3.groupby(['Classe', 'Nome']).sum()