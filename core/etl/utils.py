import json
import pandas as pd

def normalize_df(df,columns):
    for column in columns:
        df[column] = df[column].apply(json.loads)
        df_expanded = pd.json_normalize(df[column])
        df = pd.concat([df, df_expanded], axis=1)
    return df