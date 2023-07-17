#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
Prepare jdd badges input

BE AWARE THAT :
- CSV MUST CONTAINS COLUMNS 'Nom' AND 'Prénom'
- CANNOT PROCEED EXCEL FILES
"""
import pandas as pd

def create_file(input_file, output) : 

    print('Formatting data.....\n')
    if ".csv" in input_file :
        df = pd.read_csv(input_file)
    else :
        raise IOError('File extension not supported. Must be .csv')
    df = df.sort_values(by="Nom")
    df['Nom'] = df['Nom'].apply(lambda x: x.title().strip())
    df['Prénom'] = df['Prénom'].apply(lambda x: x.title().strip())
    last_names = df['Nom'].to_list()
    first_names = df['Prénom'].to_list()
    list_combined = tuple(zip(last_names, first_names))
    print('Writing tex file .....')
    with open(output,'w') as file :
        for item in list_combined :
            file.write(r"\confpin{%s}{%s}" % item)
        print('Done')
    print("File created under %s" %output)