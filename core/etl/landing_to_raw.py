import confuse
from pathlib import Path
from transformations import *
import json

project_path = str(Path(__file__).resolve().parents[2])
config = confuse.Configuration('Data_challenge_stensul', __name__)
config.set_file(project_path + '/core/config/config.yml')

def main_execution(csv_name):
    try:
        csv_path = project_path + config['directories']['landing'].get() + csv_name
        destination_path = project_path + config['directories']['raw'].get()

        df = pd.read_csv(csv_path)
        df_json = landing_to_raw_transform(df)

        with open(destination_path + "raw_input.txt", "w") as file:
            file.write(df_json)

    except Exception as e:
        return  json.dumps({"error message": str(e)})

    return '200'