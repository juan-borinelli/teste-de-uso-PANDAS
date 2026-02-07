import pandas as pd

df1 = pd.read_csv('example_file.csv', sep=',', decimal='.', parse_dates=True) #sep = separador 
#dec = termo para separar decimais 
#index_col = referencia quem é o index
#parse_dates = procura datas no conteúdo e tenta atribuir valor temporal a elas
df1.info()

df1.to_csv('exemplo_finalizado.csv', sep=';', decimal=',')
