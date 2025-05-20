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
dic={"Setor":[],'Mes':[],'Ano':[],'Valor_previsto':[],"Valor_realizado":[]}

linhas = drive.find_elements(By.TAG_NAME, 'tr')
for linha in linhas[1:]:  # Ignora o cabeçalho
    try:
        colunas = linha.find_elements(By.TAG_NAME, 'td')
        if len(colunas) >= 6:
            seto = colunas[0].text
            mes = colunas[1].text
            ano = colunas[2].text
            valoP = colunas[3].text
            valorR = colunas[4].text

            print(f'{seto}--{mes}--{ano}--{valoP}--{valorR}') 

            dic['Setor'].append(seto)
            dic['Mes'].append(mes)
            dic['Ano'].append(ano)
            dic['Valor_previsto'].append(valoP)
            dic['Valor_realizado'].append(valorR)
           
    except Exception as e:
        print("erro ao coletar os dados:", e)

drive.quit()
df = pd.DataFrame(dic)
df.to_excel("orcamento.xlsx", index=False)
print("Dados coletados com sucesso")
