import matplotlib.pyplot as plt
from colorama import init as colorama_init
from colorama import Fore, Style

colorama_init()


def make_stats(df, outdir):
    """
    make_stats Make some stats about JDDs attendees.

    Give : Number of expected participants, organized by purpose and a pie chart about how many people grouped by laboratory.

    Args:
        df (pandas.DataFrame): dataframe containing all participants.
        year (String): Year of the JDDs concerned. Used to recognize the right column in df.

    Returns:
        None
    """
    print(f"{Fore.BLUE}Creating stats about current JDDs{Style.RESET_ALL}")
    attendees = df[df['JDD'].str.contains("ASSISTER")]
    posters = df[df['JDD'].str.contains("POSTER")]
    presentations = df[df['JDD'].str.contains("ORAL")]
    with open(outdir + "stats.txt", 'w') as f:
        f.write(
            "==============================================\n"
            "\n"
            "                STATISTIQUES JDDS             \n"
            "\n"
            "==============================================\n"
            "RECENSEMENT MAXIMUM :\n"
            f"Nombre d'attendees maximal : {len(attendees)}\n"
            f"Nombre de posters : {len(posters)}\n"
            f"Nombre de présentations maximales : {len(presentations)}\n"
            f"Nombre total élèves : {len(df)}\n"
            "==============================================\n"
        )
    nb_attendees_real = len(attendees) - len(attendees.loc[attendees["Commentaires"]
                                                           .str
                                                           .contains("exempté", na=False)])
    nb_posters_real = len(posters) - len(posters.loc[posters["Commentaires"]
                                                     .str
                                                     .contains("absent aux JDD", na=False)])
    nb_oral_real = len(presentations) - len(presentations.loc[presentations["Commentaires"]
                                                              .str
                                                              .contains("cotutelle", na=False)])
    with open(outdir + "stats.txt", 'a') as f:
        f.write(
            "\n"
            "==============================================\n"
            "RECENSEMENT RÉEL : \n"
            f"Nombre d'assistants réels : {nb_attendees_real}\n"
            f"Nombre de poster réels : {nb_posters_real}\n"
            f"Nombre de présentations réelles : {nb_oral_real}\n"
            f"Nombre de doctorants réels total : {nb_attendees_real + nb_posters_real + nb_oral_real}\n"
            "==============================================\n"
        )
    count_attendees = attendees.groupby("Labo")["Nom"].count().reset_index(name='nb_doctorant')
    count_posters = posters.groupby("Labo")["Nom"].count().reset_index(name='nb_doctorant')
    count_prez = presentations.groupby("Labo")["Nom"].count().reset_index(name='nb_doctorant')
    with open(outdir + "stats.txt", "a") as f:
        f.write("STATS PAR LABO \n"
                "=============================================\n"
                "NOMBRE DE 1ERE ANNEE\n"
                )
        count_attendees.to_csv(f, header=None, index=None, sep=':')
        f.write("=============================================\n"
                "NOMBRE DE POSTERS\n")
        count_posters.to_csv(f, header=None, index=None, sep=':')
        f.write("=============================================\n"
                "NOMBRE DE PRESENTATIONS\n")
        count_prez.to_csv(f, header=None, index=None, sep=':')
    print("Done")
    print(f"{Fore.GREEN}{Style.BRIGHT}File created under {outdir} directory{Style.RESET_ALL}")
    print(f"{Fore.BLUE}Creating pie charts...{Style.RESET_ALL}")

    def formatter(x):
        return f"{total*x/100:.0f}"

    df_stats = df.groupby("Labo")["Nom"].nunique()
    total = df_stats.sum()
    plt.figure()
    df_stats.plot.pie(y="Nom", autopct=formatter)
    plt.savefig(outdir + "Stats participants JDD.png")
    df_stats_prez = presentations.groupby('Labo')['Nom'].nunique()
    total = df_stats_prez.sum()
    plt.figure()
    df_stats_prez.plot.pie(y="Nom", autopct=formatter)
    plt.savefig(outdir + "Stats presentations JDD.png")
    print('Done')
    print(f"{Fore.GREEN}{Style.BRIGHT}Pie charts created under {outdir} directory{Style.RESET_ALL}")
