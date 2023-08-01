import pandas as pd

def read_file(filename, sheetname_ensma, sheetname_up):
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


def create_namefiles(df, output_name):
    df_noms = df[['Nom', 'Prénom']]
    df_noms.to_csv(output_name + '.csv')