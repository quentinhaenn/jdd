#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
    Prepare jdd emargement list

USAGE : python3 names_to_emargement.py INPUT_FILE OUTPUT FILE
"""

from argparse import ArgumentParser
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

def main():
    parser = ArgumentParser(
       description='Generate an input .tex file to create jdd emargment lists'
    )
    parser.add_argument('input_file',
                        help='input-file containing name and first name colmuns with all attending students')
    parser.add_argument('output_file',
                        help='name of the output file produced')
    args = parser.parse_args()
    create_file(args.input_file, args.output_file)
    print("File created under %s" %args.output_file)

if __name__ == '__main__' :
    main()