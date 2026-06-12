# Entender a necessidade do solicitante. (cidade e caso de roubos de veículos desde 2003 até 2026(atual))
# Onde consigo os dados para o trabalho?
# Criar o ambiente virtual e ativar
# Instalar as bibliotecas necessárias

# fonte de informação e do arquivo estudado: 
# https://www.ispdados.rj.gov.br/estatistica.html
# https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv

#--------------------------------------------------------------------------------------------------------------#
# Bibliotecas
import os
import pandas as pd 
import numpy as np 

# Limpeza do terminal
os.system('cls')

# Obtenção dos dados dos estudos
try:
    print('Obtendo os dados...')
    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    # utf-8, iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep= ';', encoding= 'iso-8859-1')
    
    # conferencia dos dados obtidos
    #print(df_ocorrencias.head())

    # delimitando as variáveis
    df_roubo_veiculo = df_ocorrencias[['munic', 'roubo_veiculo']]
    
    # Checando o dataframe delimitado
    #print(df_roubo_veiculo.head(50))

    # Totalizando os roubos por municipios
    df_roubo_veiculo = df_roubo_veiculo.groupby('munic', as_index=False)['roubo_veiculo'].sum( ) # as_index=False para retornar com os números de indices

    # Organizando por ordem decrescente
    df_roubo_veiculo = df_roubo_veiculo.sort_values(by='roubo_veiculo', ascending=False)

    # Checando o agrupamento por cidade
    #print(df_roubo_veiculo.head(25))

except Exception as e:
    print(f'Erro ao obter dados {e}')


# Obtendo as medidas
try:
    print('Calculando as medidas... ')
    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo']) # array é uma estrutura do numpy com ganho computacional

    media_roubo_veiculo = np.mean(array_roubo_veiculo)
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)
    distancia = abs((media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo * 100) # abs é para obtermos o valor absoluto

    # Verificando as medidas estatísticas
    print('\nMedidas de Tendência Central ')
    print(50*"=")
    print(f'Média: {media_roubo_veiculo:.2f}')
    print(f'Mediana: {mediana_roubo_veiculo:.2f}')
    print(f'Distância: {distancia:.2f}%')
    
except Exception as e:
    print(f'Erro ao processar as medidas {e}')

# quando for de 0 a 10% = tendencia a serem dados simetricos  - dados considerados homogeneos 
# quando for de 10 a 25% = tendencia a ter uma assimetria moderada
# quando for acima de 25% = tendencia de assimetria forte - dados heterogeneos
