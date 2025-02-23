from transformations import *
import confuse
from pathlib import Path
import json

project_path = str(Path(__file__).resolve().parents[2])
config = confuse.Configuration('Data_challenge_stensul', __name__)
config.set_file(project_path + '/core/config/config.yml')

def main_execution(raw):
    raw_path = project_path + config['directories']['raw'].get()
    df = pd.read_json(raw_path + raw, lines=True)
    df["raw"] = df["raw"].apply(json.loads)
    df_expanded = pd.json_normalize(df["raw"])
    print(df_expanded.columns)
    #print(df_expanded)
    #df_final = df.drop(columns=["raw"]).join(df_expanded)
    #print(df_final)

    return "Hello World!"

main_execution('raw_output.txt')