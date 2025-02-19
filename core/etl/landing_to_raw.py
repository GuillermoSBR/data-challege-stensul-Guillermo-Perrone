import pandas as pd
import confuse
from pathlib import Path
import json

project_path = str(Path(__file__).resolve().parents[2])
config = confuse.Configuration('Data_challenge_stensul', __name__)
config.set_file(project_path + '/core/config/config.yml')

def main_execution(csv_name):
    try:
        csv_path = project_path + config['directories']['landing'].get() + csv_name
        destination_path = project_path + config['directories']['raw'].get()

        df = pd.read_csv(csv_path)
        df['raw'] = df.apply(lambda row: row.to_json(), axis=1)
        df_metadata_columns = df[['user_id', '_job_batch_runtime', '_job_batch_id','raw']]
        df_json = "\n".join(df_metadata_columns.apply(lambda row: row.to_json(), axis=1))

        with open(destination_path + "raw_output.txt", "w") as file:
            file.write(df_json)
    except Exception as e:
        return  json.dumps({"message": str(e)})

    return '200'