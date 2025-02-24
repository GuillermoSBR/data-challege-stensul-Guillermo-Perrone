import pandas as pd
import json
from datetime import datetime

def landing_to_raw_transform(df):
    df['raw'] = df.apply(lambda row: row.to_json(), axis=1)
    df_metadata_columns = df[['user_id', '_job_batch_runtime', '_job_batch_id', 'raw']]
    df_json = "\n".join(df_metadata_columns.apply(lambda row: row.to_json(), axis=1))
    return df_json

def inputs_table_transform(df):
    df["raw"] = df["raw"].apply(json.loads)
    df_expanded = pd.json_normalize(df["raw"])
    df_filtered = df_expanded.filter(items=['user_id', 'order_number', 'total_price_usd', 'total_price'])
    df_filtered["id"] = range(1, len(df) + 1)
    df_filtered["timestamp"] = int(datetime.now().timestamp())
    df_filtered = df_filtered.reindex(columns= ['id', 'user_id', 'order_number', 'total_price_usd', 'total_price', 'timestamp'])
    df_filtered = df_filtered.astype({'id': 'int', 'user_id':'int', 'order_number':'int', 'total_price_usd':'float',
                                      'total_price':'float', 'timestamp':'string'})
    return df_filtered

