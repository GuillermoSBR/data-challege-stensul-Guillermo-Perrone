import pandas as pd


def landing_to_raw():
    df = pd.read_csv('../db/landing/ecommerce/orders/839012383812.csv') #TODO CAMBIAR ESTO
    print(df.columns)
    df_metadata_columns = df[['user_id', '_job_batch_runtime', '_job_batch_id']]
    print(df_metadata_columns)
    df_json = df_metadata_columns.apply(lambda row: {
        "daton_user_id": row['user_id'],
        "daton_batch_runtime": row['_job_batch_runtime'],
        "daton_batch_id": row['_job_batch_id']
    }, axis=1)

    with open('output.txt', 'w') as file:
        for json_obj in df_json:
            file.write(f"{json_obj}\n")

landing_to_raw()
