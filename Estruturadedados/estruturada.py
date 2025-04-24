#excel
#pip install pandas
#pip install openpyxl
import pandas as pd


#Dicionario
dados1={
    "nome":["Iara","Pudim","Frederico","Maria"],
    "idade":[17,8,10,79],
    "cidade":["Sao Paulo","Rio de janeiro","Curitiba","Sao caetano"]
}

#dataframe

df_planilha1= pd.DataFrame(dados1)

#EXCEL

with pd.ExcelWriter("dadosestruturados.xlsx") as writer:

    df_planilha1.to_excel(writer, sheet_name= "Planilha1", index= False)


