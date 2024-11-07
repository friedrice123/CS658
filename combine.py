import pandas as pd
import os

# Set the directory containing your CSV files
directory = 'CSV_Dataset\Combined_wo_TD'

# List to hold data from each CSV file
dataframes = []

# Loop through every file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        # Construct full file path
        file_path = os.path.join(directory, filename)
        # Read the CSV file and append it to the list
        dataframes.append(pd.read_csv(file_path))
    else:
        continue

# Combine all dataframes into a single dataframe
combined_df = pd.concat(dataframes, ignore_index=True)

# Save the combined dataframe to a new CSV file
combined_df.to_csv('Combined_CSV_Dataset\Combined_wo_TD.csv', index=False)
