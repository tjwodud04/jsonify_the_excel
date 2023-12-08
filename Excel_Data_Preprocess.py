import json
import pandas as pd
import openpyxl

def excel_prerocecss(path) :
    "Making the Excel file as a dataframe"

    dataframe_from_excel = pd.read_excel(
        path,
        engine='openpyxl',
        header=0
    )

    dataframe_from_excel["질문"] = dataframe_from_excel["질문"].str.replace(
        pat=r"^[0-9]+\.",
        repl="",
        regex=True
    ) # If the contents of the "질문" column start with number (ex. 10.), delete that number

    dataframe_from_excel = dataframe_from_excel.dropna() # If the dataframe has NaN, drop that column

    number_list = list() # Making a list

    for i in range(len(dataframe_from_excel)) :
        number_list.append(i) # Making an id list

    dataframe_from_excel.insert(
        loc = 0,
        column = 'id',
        value = number_list
    ) # Insert the id list to the current dataframe

    dataframe_from_excel.columns = ["id", "question", "answer"] # Rename headers of columns

    return dataframe_from_excel

def jsonify_the_data(dfname, savename) :
    dfname.to_json(savename, orient='records', force_ascii=False, indent=4) # Save the dataframe without breaking Korean


if __name__ == '__main__':
    dataframe = excel_prerocecss(path="data/something.xlsx")
    jsonify_the_data(dfname=dataframe, savename="something.json")