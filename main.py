# Bibliotecas necessárias
# pandas, numpy, matplotlib, seaborn

import pandas as pd  # Manipulação de dados
import numpy as np   # Computação numérica (médias, desvios-padrão, correlações.)
import matplotlib.pyplot as plt  # Visualização de dados (gráficos, histogramas.)
import seaborn as sns            #     ""       ""   ""       ""        ""
# import statsmodels as sm # Modelagem estatística (regressão linear, ANOVA, etc.)

def mostrar_dataset():
  # Mostra as 5 primeiras linhas do dataset
    print(df.head(), "\n")  

def tamanho_dataset():
  # Mostra o tamanho do dataset (linhas e colunas)
    print(f"O dataset possui {df.shape[0]} linhas e {df.shape[1]} colunas.\n")

def mostrar_colunas():
  # Mostra as Variáveis do dataset
    colunas_por_linha = 6
    largura_fixa = 22

    for i, col in enumerate(df.columns, 1):
        print(col.ljust(largura_fixa), end='')
        if i % colunas_por_linha == 0:
            print()
    print()

def v_qualitativas():
  # Mostra as Variáveis Qualitativas
  colunas_por_linha = 3
  largura_fixa = 22
  
  for i, col in enumerate(['ID', 'Name', 'Type 1', 'Type 2', 'Classification_info','gen'], 1):
      print(col.ljust(largura_fixa), end='')
      if i % colunas_por_linha == 0:
          print()
  print()
  
def v_quantitativas():
  # Mostra as Variáveis Quantitativas
  colunas_por_linha = 4 #29
  largura_fixa = 22

  for i, col in enumerate(['HP', 'Attack', 'Defense', 'Sp.Attack', 'Sp.Defense', 'Speed', 'Base_Stats', 'normal_weakness', 'fire_weakness', 'water_weakness', 'electric_weakness', 'grass_weakness', 'ice_weakness', 'fighting_weakness', 'poison_weakness', 'ground_weakness', 'flying_weakness', 'psychic_weakness', 'bug_weakness', 'rock_weakness', 'ghost_weakness', 'dragon_weakness', 'dark_weakness', 'steel_weakness', 'fairy_weakness', 'number_immune', 'number_not_effective', 'number_normal', 'number_super_effective'], 1):
      print(col.ljust(largura_fixa), end='')
      if i % colunas_por_linha == 0:
          print()
  print('\n')

def sair():
  # Sai do programa
    print("Saindo...")
    exit()

df = pd.read_csv('pokemon_data.csv')  # Carrega o Dataset para um DataFrame (tabela)

acoes = {
  1: sair,
  2: mostrar_dataset,
  3: tamanho_dataset,
  4: mostrar_colunas,
  5: v_qualitativas,
  6: v_quantitativas
}

while True:
  print("| 1 - Sair |\t| 2 - Dataset |\t| 3 - Tamanho do Dataset |\t| 4 - Variáveis |\n| 5 - V_Qualitativas |\t| 6 - V_Quantitativas |\n")
  
  try:
    op = int(input("Digite a opção desejada: "))
    acao = acoes.get(op)
    
    if acao:
      acao()
    else:
      print("Opção inválida. Tente novamente.")
      
  except ValueError:
    print("Digite um número válido.")

# 1. Importar as bibliotecas necessárias para trabalhar com dados em Python.
# 2. carregar seu dataset para dentro do ambiente de trabalho
# 3. Visualizar as primeiras linhas do dataset para entender como estão organizadas.
#  - Linhas (Reg)
#  - Colunas
# 4. Descobrir o tamanho do Dataset.
# 5. Listar todas as variáveis disponíveis no dataset
# 6. Identificar o tipo de dado de cada variável.
#  - Qualitativa
#    {Name, abilities, type1, type2, Classificatio generation, legendary}
#  - Quantitativa
#    {HP, Attack, Defense, Sp. Atk, Sp. Def, Speed, Total}
# 7. Organizar essa classificação em uma pequena tabela para visualização.