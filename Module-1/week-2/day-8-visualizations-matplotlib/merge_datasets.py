import pandas as pd

<<<<<<< HEAD
def merge_intake_outcomes(data1,data2):
=======
def merge_intake_outcomes(data1, data2):
>>>>>>> b9c45f5bd91b390143aa6ebf891e009ecc53521f
    """
    This function:
        - merges intake_dataset with outcomes_dataset
        - creates new variable `days_in_shelter`
        - returns animal_shelter_df
    """
<<<<<<< HEAD
    animal_shelter_df  = pd.merge(data1, data2, on=['id', 'year'],how='left', suffixes=('_intake', '_outcome'))
=======
    animal_shelter_df  = pd.merge(data1, data2, on=['id', 'year'], how='left', suffixes=('_intake', '_outcome'))
>>>>>>> b9c45f5bd91b390143aa6ebf891e009ecc53521f

    animal_shelter_df = animal_shelter_df[(~animal_shelter_df['o_date'].isna()) &                                           (animal_shelter_df['o_date'] > animal_shelter_df['i_date'])]

    animal_shelter_df['days_in_shelter'] = (animal_shelter_df['o_date'] - animal_shelter_df['i_date']).dt.days
    return animal_shelter_df

                                                              

