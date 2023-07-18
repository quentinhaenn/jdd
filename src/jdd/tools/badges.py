"""
Prepare jdd badges input

BE AWARE THAT :
- CSV MUST CONTAINS COLUMNS 'Nom' AND 'Prénom'
- CANNOT PROCEED EXCEL FILES
"""
import pandas as pd
import os
from colorama import Fore, Style
from colorama import init as colorama_init

colorama_init()
print(os.getcwd())

def create_file(input_file, output) :
    print(f"{Fore.BLUE}Creating badge file...{Style.RESET_ALL}")
    print(f'{Fore.BLUE}Formatting data .....{Style.RESET_ALL}')
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
    print(f'{Fore.BLUE}Writing tex file .....{Style.RESET_ALL}')
    with open(output,'w') as file :
        for item in list_combined :
            file.write(r"\confpin{%s}{%s}" % item)
        print('Done')
    print(f"{Fore.GREEN}{Style.BRIGHT}File created under {output}{Style.RESET_ALL}")
