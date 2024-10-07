import json
import pandas as pd

# Specify the path to your JSON file
json_file_path = 'CICDataset_Organized\CICDataset_Organized\Dataset\Wrong_EV_TS\Random_CS_Off\Gaussian_Off\STAT\CS\STAT.json'
json_name = 'WEVTS_RCSOFF_GOFF_CS'

def process_stats(file_path):
    # Open and load the JSON data from the file
    with open(file_path, 'r') as file:
        data = json.load(file)

    records = []
    for key, values in data.items():
        for condition, metrics in values['branch'].items():
            record = {
                'id': key,
                'condition': condition,
                'mean_stat': sum(metrics['data_point']) / len(metrics['data_point']),
                'max_stat': max(metrics['data_point']),
                'min_stat': min(metrics['data_point']),
                'std_stat': pd.Series(metrics['data_point']).std(),
                'sampling_count': metrics['sampling_count'],
                'simulation_time': metrics['simulation_time'],
                'sampling_resolution': metrics['sampling_resolution']
            }
            records.append(record)
    return pd.DataFrame(records)

# Load data and process it
df = process_stats(json_file_path)

# Example to save to CSV
df.to_csv(f'Stat\S_{json_name}.csv', index=False)
