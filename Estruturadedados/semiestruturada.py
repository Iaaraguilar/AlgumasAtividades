#Json
import pandas as pd



#Dicionario
dadosjson={
    "nome":["Iara","Pudim","Frederico","Maria"],
    "idade":[17,8,10,79],
    "cidade":["Sao Paulo","Rio de janeiro","Curitiba","Sao caetano"]
}

#dataframe

df_json= pd.DataFrame(dadosjson)

#salvar em json

df_json.to_json("dadossemi.json",orient= "records",lines=False)

