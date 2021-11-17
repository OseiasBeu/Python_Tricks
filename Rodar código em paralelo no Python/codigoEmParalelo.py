import time
import os
import pandas as pd
from joblib import Parallel, delayed

tempo_inicial = time.time()

arquivos = os.listdir()

tabela_final = pd.DataFrame()
for arquivo in arquivos:
    if "xlsx" in arquivo:
        tabela = pd.read_excel(arquivo)
        faturamento = tabela["Valor Final"].sum()
        print(f"Faturamento da Loja {arquivo.replace('.xlsx', '')} foi de R${faturamento: 2f}")
        
print(f"Demorou: {time.time() - tempo_inicial}")



tempo_inicial2 = time.time()
arquivos = os.listdir()
def calcular_faturamento(arquivo):
    if "xlsx" in arquivo:
        tabela = pd.read_excel(arquivo)
        faturamento = tabela['Valor Final'].sum()
        return f"Faturamento da loja {arquivo.replace('.xlsx','')} for de R${faturamento:.2f}"

resultado = Parallel(n_jobs=2)(delayed(calcular_faturamento)(arquivo) for arquivo in arquivos)
print(resultado)
print(f"Demorou: {time.time() - tempo_inicial2}")