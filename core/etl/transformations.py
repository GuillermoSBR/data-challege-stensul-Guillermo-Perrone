from datetime import datetime
from utils import *

def landing_to_raw_transform(df):
    df_raw_data = df.filter(items=['_job_user_id', '_job_batch_runtime', '_job_batch_id'])
    df_no_job_columns = df.drop(['_job_user_id', '_job_batch_runtime', '_job_batch_id'], axis=1)
    df_raw_data['data_raw'] = df_no_job_columns.apply(lambda row: row.to_json(), axis=1)
    df_raw_data["creation_ts"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df_raw_data = df_raw_data.reindex(columns=['data_raw','_job_user_id', '_job_batch_runtime', '_job_batch_id', 'creation_ts'])
    df_json = "\n".join(df_raw_data.apply(lambda row: row.to_json(), axis=1))
    return df_json

def inputs_table_transform(df):
    df_norm = normalize_df(df,['data_raw'])
    df_filtered = df_norm.filter(items=['user_id', 'order_number', 'total_price_usd', 'total_price','creation_ts'])
    df_filtered["id"] = range(1, len(df_norm) + 1)
    df_filtered['creation_ts'] = pd.to_datetime(df_filtered['creation_ts'])
    df_filtered['creation_ts'] = df_filtered['creation_ts'].apply(lambda x: int(x.timestamp()))
    df_filtered = df_filtered.reindex(columns= ['id', 'order_number', 'user_id',  'total_price_usd', 'total_price', 'creation_ts'])
    df_filtered = df_filtered.astype({'id': 'int', 'user_id':'int', 'order_number':'int', 'total_price_usd':'float',
                                      'total_price':'float', 'creation_ts':'string'})
    return df_filtered

def metrics_table_transform(df):
    df_orders_metrics = (
        df.groupby('creation_ts').agg(total_orders_qty=('order_number', 'count'), total_sales_amount=('total_price', 'sum')).reset_index()
    )
    df_orders_metrics['creation_dt'] = pd.to_datetime(df_orders_metrics['creation_ts'].astype(int), unit='s', utc=True).dt.date
    df_orders_metrics = df_orders_metrics.drop('creation_ts', axis=1)
    df_orders_metrics = df_orders_metrics.reindex(columns=['creation_dt', 'total_orders_qty', 'total_sales_amount'])
    df_orders_metrics = df_orders_metrics.astype({'total_orders_qty': 'int', 'total_sales_amount': 'float'})

    return df_orders_metrics