import pandas as pd
import tools.stats as stats
import tools.badges as badges
import tools.signing_lists as signing
import tools.qrcodes as qrcodes
import os
from argparse import ArgumentParser
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

OUTDIR = "out/"
RESOURCEDIR = "src/resource/"
TEXDIR = "out/tex/"

if not os.path.isdir(OUTDIR) :
    os.mkdir(OUTDIR)

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
    parser.add_argument("-qr", "--qr-code",
                        action='store_true',
                        help='When used, will prompt the commands to create qr codes from urls and generate png files.'
                        )
    args = parser.parse_args()
    print(args)
    print(os.getcwd())
    df_participants, df_ensma, df_up = read_file(
        RESOURCEDIR + args.input_file, "ENSMA", "UP"
        )

    if os.path.exists(RESOURCEDIR + "noms_ensma.csv") :
        os.remove(RESOURCEDIR + "noms_ensma.csv")
        os.remove(RESOURCEDIR + "noms_up.csv")
        os.remove(RESOURCEDIR + "noms_complet.csv")

    print(f"{Fore.BLUE}Creating name files...{Style.RESET_ALL}")
    create_namefiles(df_ensma, RESOURCEDIR + "noms_ensma")
    create_namefiles(df_up, RESOURCEDIR + "noms_up")
    create_namefiles(df_participants, RESOURCEDIR + "noms_complet")
    print('Done')
    print(f"{Fore.GREEN}{Style.BRIGHT}File created under '{RESOURCEDIR} directory{Style.RESET_ALL}")

    if args.badges :
        badges.create_file(RESOURCEDIR + "noms_complet.csv", TEXDIR + "badges.tex")

    if args.signing_pages :
        signing.create_file(RESOURCEDIR + "noms_ensma.csv", TEXDIR + "list_ensma.tex")
        signing.create_file(RESOURCEDIR + "noms_up.csv", TEXDIR + "list_up.tex")


    if args.make_stats :
        stats.make_stats(df_participants, OUTDIR)
    
    if args.qr_code :
        qrcodes.make_qr(OUTDIR)

    if not (args.badges or args.signing_pages or args.make_stats or args.qr_code) :
        badges.create_file(RESOURCEDIR + "noms_complet.csv", TEXDIR + "badges.tex")
        signing.create_file(RESOURCEDIR + "noms_ensma.csv", TEXDIR + "list_ensma.tex")
        signing.create_file(RESOURCEDIR + "noms_up.csv", TEXDIR + "list_up.tex")
        stats.make_stats(df_participants, OUTDIR)
    

    print(f"{Fore.GREEN}=====================================\n"
          f"Every task has been done successfully.\n"
          f"====================================={Style.RESET_ALL}")

if __name__ == '__main__':
    main()
