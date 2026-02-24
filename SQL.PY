import sqlite3
import pandas as pd

conection = sqlite3.connect('web.db')
df_data = pd.read_csv('exemplo_finalizado.csv', index_col=0, sep=';', decimal=',')

df_data.index.name = 'index_name'
df_data.to_sql('data', conection, index_label='index_name') # passando um DF para o DB


#ponteiro na db
c = conection.cursor() # ponteiro (especie de interpretador de interacao do pandas com SQL)

#criando tabela
c.execute('CREATE TABLE products (product_id, product_name, price)') #chama o interpretador, exigindo o codigo para SQL
conection.commit() # comando para salvar alteracoes

#deletando tabela
c.execute('DROP TABLE products') #eliminado tabela 'products'
c.execute('DROP TABLE data') #eliminando tabela 'data'

c.execute('CREATE TABLE products ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT, [price] INTEGER)')
# criando tabela products com o type de cada coluna definido

# INSERT
c.execute('''INSERT INTO products (product_id, product_name, price)
          VALUES
          (1, 'Computer', 800),
          (2, 'Printer', 200),
          (3, 'Tablet', 300)
          ''')
conection.commit()

df_data2 = df_data.iloc[::-2]
df_data2.to_sql('data', conection, if_exists='append')

# SELECT
c.execute('SELECT * FROM data')
c.fetchone() # retorna a primeira execucao da nossa DB
c.fetchall() # retorna todas as execucoes da nossa DB

df = pd.DataFrame(c.fetchall())
df
# (NAO EH CONSIDERADO BOA PRATICA) para salvar a DF atraves do fetchall, eh necessario que de o comando do 'execute(select)' e em seguida ja realize o comando de criacao da DF atraves do fetchall

# Selecionando todos os dados de DATA que correspondem a selecao de filtros
c.execute('SELECT * FROM data WHERE Proven_Reserves_Billion_Barrels > 6.5 AND Estimated_Recoverable_Reserves_Billion_Barrels > 4')
df = pd.DataFrame(c.fetchall())
df

# Selecionando algumas colunas de DATA que correspondem aos filtros
c.execute('SELECT Reservoir_Name, Basin_Region, Location FROM data WHERE Proven_Reserves_Billion_Barrels > 6.5 AND Estimated_Recoverable_Reserves_Billion_Barrels > 4')
df = pd.DataFrame(c.fetchall())
df


# CARREGANDO DADOS de uma DB ATRAVES DO "READ_SQL" no Pandas (melhor forma)
query = 'SELECT * FROM data' # a requisicao que sera feita ao DB eh adicionada na variavel 'query'
df_query = pd.read_sql(query, con=conection, index_col='index_name') # MELHOR forma de carregar os dados de uma DB pelo pandas
df_query

query1 = 'SELECT Reservoir_Name, Basin_Region, Location FROM data WHERE Proven_Reserves_Billion_Barrels > 6.5 AND Estimated_Recoverable_Reserves_Billion_Barrels > 4'
df_query1 = pd.read_sql(query1, con=conection)
df_query1


# UPDATE e DELETE
c.execute('UPDATE data SET Status="Active" WHERE index_name=1 ') # atualizando valor na coluna 'Status' no index 1
conection.commit() # aplicando atualizacao ao banco de dados

c.execute('UPDATE data SET Status="Development (alt)", Year_Discovered=2026 WHERE index_name=1') # realizando alteracao no status e no 'year_discovered'
conection.commit()
# df_data2.to_sql('data', conection, if_exists='replace') -> exemplo para esse comando no PANDAS


#delete joga fora entradas(linhas), drop joga fora tabela ou banco de dados
c.execute('DELETE FROM data WHERE index_name=1') # excluindo linha de index=1
conection.commit()