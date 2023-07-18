"""
    Prepare jdd emargement list
"""
import pandas as pd
from colorama import init as colorama_init
from colorama import Fore, Style

colorama_init()

def create_file(input_file, output_file) :
    print(f"{Fore.BLUE}Creating signing lists files...{Style.RESET_ALL}")
    print(f'{Fore.BLUE}Formatting data .....{Style.RESET_ALL}')
    if '.csv' in input_file :
        df = pd.read_csv(input_file)
    else :
        raise IOError('File extension not supported. Must be .csv')
    df = df.sort_values(by='Nom')
    df['Nom'] = df['Nom'].apply(lambda x: x.title().strip())
    df['Prénom'] = df['Prénom'].apply(lambda x: x.title().strip())
    last_names = df['Nom'].to_list()
    first_names = df['Prénom'].to_list()
    list_combined = tuple(zip(last_names, first_names))
    print(f'{Fore.BLUE}Writing tex file .....{Style.RESET_ALL}')
    with open(output_file,'w') as file :
        for item in list_combined :
            file.write(r"\Large\textsc{%s} & \Large %s &  &  &  \\ \hline" % item)
            file.write("\n")
        print('Done')
    print(f"{Fore.GREEN}{Style.BRIGHT}File created under {output_file}{Style.RESET_ALL}")