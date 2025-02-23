import pandas as pd

def landing_to_raw_transform(df):
    df['raw'] = df.apply(lambda row: row.to_json(), axis=1)
    df_metadata_columns = df[['user_id', '_job_batch_runtime', '_job_batch_id', 'raw']]
    df_json = "\n".join(df_metadata_columns.apply(lambda row: row.to_json(), axis=1))
    return df_json

