"""
    Prepare jdd emargement list
"""
import pandas as pd

def create_file(input_file, output_file) :
    print("Formatting data ... \n")
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
    print('Writing tex file .....')
    with open(output_file,'w') as file :
        for item in list_combined :
            file.write(r"\Large\textsc{%s} & \Large %s &  &  &  \\ \hline" % item)
            file.write("\n")
        print('Done')
    print("File created under %s" %output_file)