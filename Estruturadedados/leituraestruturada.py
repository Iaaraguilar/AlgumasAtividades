import pandas as pd

dfexcel= pd.read_excel("dadosestruturados.xlsx", sheet_name=["Planilha1"])

#dfaba1=dfexcel["Planilha1"]
#dfaba2=dfexcel["Planilha1"]
               
print(dfexcel)