from transformations import *
import confuse
from pathlib import Path


project_path = str(Path(__file__).resolve().parents[2])
config = confuse.Configuration('Data_challenge_stensul', __name__)
config.set_file(project_path + '/core/config/config.yml')

def main_execution(raw):
    raw_path = project_path + config['directories']['raw'].get()
    app_path = project_path + config['directories']['app'].get()
    df = pd.read_json(raw_path + raw, lines=True)

    inputs_df = inputs_table_transform(df)
    inputs_df.to_parquet(app_path+'inputs_table.parquet', engine='pyarrow')

    metrics_df = metrics_table_transform(inputs_df)
    metrics_df.to_parquet(app_path + 'metrics_table.parquet', engine='pyarrow')

    return "Hello World!"

main_execution('raw_output.txt')