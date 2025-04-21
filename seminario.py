import matplotlib.pyplot as plt
import pandas as pd
import os
from wordcloud import WordCloud
from datetime import datetime

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    else:
        print('Sistema operacional não suportado.')

def data_valida(data_str):
    try:        
        datetime.strptime(data_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def carregar_arquivo():
    limpar_tela()
    print('Carregando arquivo "Historico_de_materias.csv"\n')
    data_frame = pd.read_csv('Historico_de_materias.csv', sep=',')
    data_frame['ano'] = 0
    data_frame['mes'] = 0
    print(data_frame)
    print('\nArquivo carregado com sucesso')
    input('\nPressione ENTER para continuar...')
    return data_frame

def alimentar_colunas_mes_e_ano():
    limpar_tela()
    print('Alimentando as colunas mes e ano\n')
    for i, row in df.iterrows():
        if data_valida(str(row['data'])):
            data = datetime.strptime(row['data'], "%Y-%m-%d")
            df.at[i, 'ano'] = data.year
            df.at[i, 'mes'] = data.month
        else:
            print(f'Data inválida encontrada na linha {i}: {row["data"]}')
    print()    
    print('Alimentação das colunas concluída com sucesso\n')
    print(df)
    input("\nPressione ENTER para continuar...")

def agrupar_materias_por_assunto():
    limpar_tela()
    print('Agrupando materias por assunto\n')
    data_frame = df.groupby('assunto').count().sort_values(by='data', ascending=False)
    print(data_frame.head)
    print('\nMaterias agrupadas com sucesso')
    input('\nPressione ENTER para continuar...')
    return data_frame

def exibir_grafico_de_materias_agrupadas_por_assunto():
    limpar_tela()
    input('\nPressione ENTER para ver o gráfico de materias por assunto. Em seguida feche a janela do gráfico para continuar.')
    plt.figure(figsize=(6, 6))
    plt.pie(materias_agrupadas_por_assunto['data'],
            labels=materias_agrupadas_por_assunto.index,
            autopct='%1.1f%%',
            startangle=90)
    plt.axis('equal')
    plt.title('Distribuição de Assuntos')
    plt.show()
    print('\nGráfico exibido com sucesso')
    input('\nPressione ENTER para continuar...')

def limpar_lista_de_palavras(lista_de_palavras):
    preposicoes = {
        "a", "ante", "após", "até", "com", "contra", "de", "desde",
        "em", "entre", "para", "perante", "por", "sem", "sob", "sobre", "trás",
        "às", "dum", "duma", "num", "numa", "ao", "aos", "na", "nas", "no", "nos",
        "da", "das", "do", "dos", "pela", "pelas", "pelo", "pelos"
    }
    conjuncoes = {
        "e", "nem", "mas", "porém", "todavia", "contudo", "entretanto", "ou", "ora", "já", "quer", "pois",
        "porque", "como", "quando", "enquanto", "logo", "embora", "ainda", "conquanto", "caso",
        "se", "desde", "que", "assim", "para", "que", "a fim", "de", "modo", "antes", "depois",
        "tão", "tanto", "quanto", "senão"
    }
    artigos = {
        "o", "a", "os", "as", "um", "uma", "uns", "umas" 
    }
    adverbios_comuns = {
        "aqui", "ali", "lá", "cá", "acolá", "hoje", "ontem", "amanhã", "já", "logo",
        "sempre", "nunca", "jamais", "antes", "depois", "ainda", "também", "muito",
        "pouco", "bastante", "demais", "tão", "tanto", "quase", "só", "somente",
        "apenas", "talvez", "certamente", "provavelmente", "sim", "não", "acaso"
    }
    outras_palavras = {"diz", "é"}
    lista_de_palavras = [p for p in lista_de_palavras if p.lower() not in preposicoes]
    lista_de_palavras = [p for p in lista_de_palavras if p.lower() not in conjuncoes]
    lista_de_palavras = [p for p in lista_de_palavras if p.lower() not in artigos]
    lista_de_palavras = [p for p in lista_de_palavras if p.lower() not in adverbios_comuns]
    lista_de_palavras = [p for p in lista_de_palavras if p.lower() not in outras_palavras]
    return lista_de_palavras


def exibir_nuvem_de_palavras_das_manchetes():
    limpar_tela()
    input('Pressione ENTER para ver a nuvem de palavras das manchetes. Em seguida feche a janela do gráfico para continuar.')    
    df_esportes = df[df['assunto'] == 'esportes']    
    lista_de_palavras_dos_titulos = limpar_lista_de_palavras(' '.join(df_esportes['titulo']).split())
    lista_de_palavras_em_fortmato_str = ' '.join(lista_de_palavras_dos_titulos)
    wc = WordCloud(width=800, height=400, max_words=100, background_color='white').generate(lista_de_palavras_em_fortmato_str)
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    print('\nNuvem de palavras exibida com sucesso')
    input('\nPressione ENTER para continuar...')

df = carregar_arquivo()
alimentar_colunas_mes_e_ano()
materias_agrupadas_por_assunto = agrupar_materias_por_assunto()
exibir_grafico_de_materias_agrupadas_por_assunto()
exibir_nuvem_de_palavras_das_manchetes()