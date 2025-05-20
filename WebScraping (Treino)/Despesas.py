from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.common.exceptions import TimeoutException
chrome_driver= r'C:\Program Files\chromedriver-win64\chromedriver.exe' 
service=Service(chrome_driver)
options=webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
drive=webdriver.Chrome(service=service,options=options)
link='https://masander.github.io/AlimenticiaLTDA-financeiro/'
drive.get(link)
time.sleep(5)
dic={"id_despesa":[],'Data':[],'Tipo':[],'Setor':[],"Valor":[],"Fornecedor":[]}

linhas = drive.find_elements(By.TAG_NAME, 'tr')
for linha in linhas[1:]:  
    try:
        colunas = linha.find_elements(By.TAG_NAME, 'td')
        if len(colunas) >= 6:
            id = colunas[0].text
            data = colunas[1].text
            tipo = colunas[2].text
            setor = colunas[3].text
            valor = colunas[4].text
            fornecedor = colunas[5].text

            print(f'{id}--{data}--{tipo}--{setor}--{valor}--{fornecedor}') 

            dic['id_despesa'].append(id)
            dic['Data'].append(data)
            dic['Tipo'].append(tipo)
            dic['Setor'].append(setor)
            dic['Valor'].append(valor)
            dic['Fornecedor'].append(fornecedor)
    except Exception as e:
        print("erro ao coletar os dados:", e)

tela=drive.find_element(By.XPATH,'//*[@id="SubPageContainer"]/div[1]/nav/button[2]')
tela.click()
dicorcamento={"Setor":[],'Mes':[],'Ano':[],'Valor_previsto':[],"Valor_realizado":[]}

line = drive.find_elements(By.TAG_NAME, 'tr')
for li in line [1:]:  # Ignora o cabeçalho
    try:
        colu = li.find_elements(By.TAG_NAME, 'td')
        if len(colu) >= 5:
            seto = colu[0].text
            mes = colu[1].text
            ano = colu[2].text
            valoP = colu[3].text
            valorR = colu[4].text

            print(f'{seto}--{mes}--{ano}--{valoP}--{valorR}') 

            dicorcamento['Setor'].append(seto)
            dicorcamento['Mes'].append(mes)
            dicorcamento['Ano'].append(ano)
            dicorcamento['Valor_previsto'].append(valoP)
            dicorcamento['Valor_realizado'].append(valorR)
           
    except Exception as e:
        print("erro ao coletar os dados:", e)
drive.quit()
with pd.ExcelWriter("financeiro.xlsx") as writer:
    pd.DataFrame(dic).to_excel(writer, sheet_name="Despesas", index=False)
    pd.DataFrame(dicorcamento).to_excel(writer, sheet_name="Planejamento", index=False)

print("Dados coletados com sucesso")