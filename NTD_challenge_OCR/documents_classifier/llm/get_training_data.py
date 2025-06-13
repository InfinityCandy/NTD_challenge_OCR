import os
import json
import pandas as pd


def get_training_data():
    PATH = "documents_classifier/data/"

    all_entries = []

    for filename in os.listdir(PATH):
        if filename.endswith(".json"):
            file_path = os.path.join(PATH, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    if isinstance(data, list):
                        all_entries.extend(data)
                except json.JSONDecodeError as e:
                    print(f"Error decoding {filename}: {e}")

    merged_df = pd.DataFrame(all_entries)

    return merged_df
