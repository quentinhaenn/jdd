import pandas as pd
import tools.stats as stats
import tools.badges as badges
import tools.signing_lists as signing
import os
from argparse import ArgumentParser
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

def read_file(filename, sheetname_ensma, sheetname_up) :
    """
    read_file : Read excel file to generate dataframe.

    Args:
        filename (String): Name of the excel file, including extension.
        sheetname_ensma (String): Name of the excel sheet concerning ensma.
        sheetname_up (String): Name of the excel sheet concerning UP

    Returns:
        df_participants, df_ensma, df_up (Tuple): Tuple containing each dataframe created, in this order.
    """
    df_participant = pd.read_excel(filename, header=2, sheet_name=None)
    df_ensma = df_participant[sheetname_ensma]
    df_up = df_participant[sheetname_up]
    df_participant = pd.concat([df_ensma, df_up])
    df_ensma.reset_index(inplace=True)
    df_up.reset_index(inplace=True)
    df_participant.reset_index(inplace=True)
    return df_participant, df_ensma, df_up

def create_namefiles(df, output_name) :
    df_noms = df[['Nom', 'Prénom']]
    df_noms.to_csv(output_name + '.csv')


def main():
    parser = ArgumentParser(
        prog="jdd/main.py",
        description='help to create badges and stuff for JDDs',
        epilog='If no option provided, will create all stuff at once'
    )
    parser.add_argument('input_file', help='Name or path of the input file')
    parser.add_argument(
        '-b','--badges',
        action='store_true',
        help='When used, create badges based on template badges.tex')
    parser.add_argument('-s', '--signing-pages',
                        action='store_true',
                        help="When used, create signing pages based on template and input file")
    parser.add_argument('-ms', '--make-stats',
                        action='store_true',
                        help="When used, create some util stats based on input file")
    args = parser.parse_args()
    print(args)
    print(os.getcwd())
    df_participants, df_ensma, df_up = read_file(
        "src/resource/Participants JDD.xlsx", "ENSMA 22-23", "UP 22-23"
        )

    if os.path.exists("src/resource/noms_ensma.csv") :
        os.remove("src/resource/noms_ensma.csv")
        os.remove("src/resource/noms_up.csv")
        os.remove("src/resource/noms_complet.csv")

    print(f"{Fore.BLUE}Creating name files...{Style.RESET_ALL}")
    create_namefiles(df_ensma, "src/resource/noms_ensma")
    create_namefiles(df_up, "src/resource/noms_up")
    create_namefiles(df_participants, "src/resource/noms_complet")
    print('Done')
    print(f"{Fore.GREEN}{Style.BRIGHT}File created under 'src/resource/ directory{Style.RESET_ALL}")

    if args.badges :
        print(f"{Fore.RED}Creating badge file...{Style.RESET_ALL}")
        badges.create_file("src/resource/noms_complet.csv", "src/tex/badges.tex")

    if args.signing_pages :
        print(f"{Fore.RED}Creating signing lists files...{Style.RESET_ALL}")
        signing.create_file("src/resource/noms_ensma.csv", "src/resource/list_ensma.tex")
        signing.create_file("src/resource/noms_up.csv", "src/resource/list_up.tex")
    

    if args.make_stats :
        print(f"{Fore.RED}Creating stats about current JDDs{Style.RESET_ALL}")
        stats.make_stats(df_participants, '2023')
        
if __name__ == '__main__':
    main()
