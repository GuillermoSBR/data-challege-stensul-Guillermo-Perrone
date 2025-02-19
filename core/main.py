import pandas as pd


def landing_to_raw():
    df = pd.read_csv('../db/landing/ecommerce/orders/839012383812.csv') #TODO CAMBIAR ESTO
    df_metadata_columns = df[['user_id', '_job_batch_runtime', '_job_batch_id']]

    df_json = df.to_json()


    with open("output.txt", "w") as file:
        file.write(df_json)

landing_to_raw()
