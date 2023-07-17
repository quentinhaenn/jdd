import pandas as pd
import matplotlib.pyplot as plt

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
    attendees = df[df['JDD ' + year].str.contains("ASSISTER")]
    posters = df[df['JDD ' + year].str.contains("POSTER")]
    presentations = df[df['JDD ' + year].str.contains("ORAL")]
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
    plt.figure()
    df_stats.plot.pie(y="Nom", autopct=formatter)
    plt.savefig("Stats participants JDD " + year + ".png")
    df_stats_prez = presentations.groupby('Labo ')['Nom'].nunique()
    total = df_stats_prez.sum()
    plt.figure()
    df_stats_prez.plot.pie(y="Nom", autopct=formatter)
    plt.savefig("Stats presentations JDD " + year + ".png")