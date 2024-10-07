import json
import numpy as np
import pandas as pd
import csv

def process_json_data_to_csv(file_path, output_csv_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    with open(output_csv_path, 'w', newline='') as csvfile:
        fieldnames = ['id', 'condition', 'type', 'field', 'mean_top', 'max_top', 'min_top', 'std_top', 'sampling_count', 'simulation_time', 'sampling_resolution']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for system_id, system_data in data.items():
            for branch_type, fields in system_data.items():
                for condition, field_data in fields.items():
                    for field, data_p in field_data.items():
                        data_points = data_p['data_point']
                        if data_points:
                            max_value = np.max(data_points)
                            min_value = np.min(data_points)
                            average_value = np.mean(data_points)
                            std_top = pd.Series(data_points).std()
                            sampling_count = data_p['sampling_count']
                            simulation_time = data_p['simulation_time']
                            sampling_resolution = data_p['sampling_resolution']
                            writer.writerow({
                                'id': system_id,
                                'condition': condition,
                                'type': branch_type,
                                'field': field,
                                'mean_top': average_value,
                                'max_top': max_value,
                                'min_top': min_value,
                                'std_top': std_top,
                                'sampling_count': sampling_count,
                                'simulation_time': simulation_time,
                                'sampling_resolution': sampling_resolution
                            })

# Example usage
file_path = 'CICDataset_Organized\CICDataset_Organized\Dataset\Wrong_EV_TS\Random_CS_On\Gaussian_Off\TOP\CS\TOP.json'
output_csv_path = 'CSV_Dataset\Top\T_WEVTS_RCSON_GOFF_CS.csv'
process_json_data_to_csv(file_path, output_csv_path)
