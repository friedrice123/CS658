import json
import pandas as pd

# Specify the path to your JSON file
json_file_path = 'CICDataset_Organized\CICDataset_Organized\Dataset\Wrong_ID\Random_CS_Off\Gaussian_Off\TIME_DELTA\TIME_DELTA.json'
json_name = 'WID_RCSOFF_GOFF'

def process_time_diffs(file_path):
    # Open and load the JSON data from the file
    with open(file_path, 'r') as file:
        data = json.load(file)

    records = []
    for key, values in data.items():
        for condition, metrics in values['time_diff'].items():
            record = {
                'id': key,
                'condition': condition,
                'mean_time_diff': sum(metrics['data_point']) / len(metrics['data_point']),
                'max_time_diff': max(metrics['data_point']),
                'min_time_diff': min(metrics['data_point']),
                'std_time_diff': pd.Series(metrics['data_point']).std(),
                'sampling_count': metrics['sampling_count'],
                'simulation_time': metrics['simulation_time'],
                'sampling_resolution': metrics['sampling_resolution']
            }
            records.append(record)
    return pd.DataFrame(records)

# Load data and process it
df = process_time_diffs(json_file_path)

# Example to save to CSV
df.to_csv(f'TD_{json_name}.csv', index=False)
