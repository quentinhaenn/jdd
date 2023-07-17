import pandas as pd
import matplotlib.pyplot as plt


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

def make_stats(df, year) :
    """
    make_stats Make some stats about JDDs attendees.

    Provide : Number of expected participants, organized by purpose and a pie chart about how many people grouped by laboratory.

    Args:
        df (pandas.DataFrame): dataframe containing all participants.
        year (String): Year of the JDDs concerned. Used to recognize the right column in df.

    Returns:
        None
    """
    attendees = df['JDD ' + year].str.contains("ASSISTER")
    posters = df['JDD ' + year].str.contains("POSTER")
    presentations = df['JDD ' + year].str.contains("ORAL")
    print(
        "RECENSEMENT MAXIMUM :\n"
        f"Nombre d'attendees maximal : {len(attendees)}\n"
        f"Nombre de posters : {len(posters)}\n"
        f"Nombre de présentations maximales : {len(presentations)}\n"
        f"Nombre total élèves : {len(df)}"
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
    print("RECENSEMENT RÉEL : \n"
          f"Nombre d'assistants réels : {nb_attendees_real}\n"
          f"Nombre de poster réels : {nb_posters_real}\n"
          f"Nombre de présentations réelles : {nb_oral_real}\n"
          f"Nombre de doctorants réels total : {nb_attendees_real + nb_posters_real + nb_oral_real}"
    )

    def formatter(x) :
        return f"{total*x/100:.0f}"
    df_stats = df.groupby("Labo ")["Nom"].nunique()
    total = df_stats.sum()
    df_stats.plot.pie(y="Nom", autopct=formatter)
    plt.savefig("Stats JDD " + year + ".png")