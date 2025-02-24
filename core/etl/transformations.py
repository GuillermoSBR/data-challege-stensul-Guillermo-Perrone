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
    df_filtered["creation_ts"] = int(datetime.now().timestamp())
    df_filtered = df_filtered.reindex(columns= ['id', 'order_number', 'user_id',  'total_price_usd', 'total_price', 'creation_ts'])
    df_filtered = df_filtered.astype({'id': 'int', 'user_id':'int', 'order_number':'int', 'total_price_usd':'float',
                                      'total_price':'float', 'creation_ts':'string'})
    print(df_filtered)
    return df_filtered

def metrics_table_transform(df):
    df_orders_metrics = (
        df.groupby('creation_ts').agg(total_orders_qty=('order_number', 'count'), total_sales_amount=('total_price', 'sum')).reset_index()
    )

    df_orders_metrics['creation_dt'] = pd.to_datetime(df_orders_metrics['creation_ts'].astype(int), unit='s', utc=True).dt.date
    df_orders_metrics = df_orders_metrics.drop('creation_ts', axis=1)
    df_orders_metrics = df_orders_metrics.reindex(columns=['creation_dt', 'total_orders_qty', 'total_sales_amount'])
    df_orders_metrics = df_orders_metrics.astype({'total_orders_qty': 'int', 'total_sales_amount': 'float'})
    print(df_orders_metrics)

    return df_orders_metrics

