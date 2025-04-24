#CSV

import pandas as pd




#Dicionario
dadosCSV={
    "nome":["Iara","Pudim","Frederico","Maria"],
    "idade":[17,8,10,79],
    "cidade":["Sao Paulo","Rio de janeiro","Curitiba","Sao caetano"]
}

#dataframe

dfcsv= pd.DataFrame(dadosCSV) 

dfcsv.to_csv("dadosnao.csv",index=False)
