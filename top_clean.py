import os
import pandas as pd

# Directory containing the CSV files
directory = "CSV_Dataset\Top"

# Output file to save the filtered data
output_file = "Combined_CSV_Dataset\Top.csv"

# Initialize an empty dataframe to store the final filtered rows
filtered_rows = pd.DataFrame()

# Loop over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(directory, filename)
        df = pd.read_csv(file_path)

        # Ensure the column names are consistent with your data
        # Group by 'id' and 'field', ensuring both 'attack' and 'normal' conditions exist
        condition_check = df.groupby(['id', 'type', 'field'])['condition'].apply(lambda x: set(x) == {'attack', 'normal'})
        
        # Filter the original dataframe to include only rows where both conditions exist
        matching_groups = condition_check[condition_check].index
        filtered_df = df[df.set_index(['id', 'type', 'field']).index.isin(matching_groups)].reset_index(drop=True)

        # Append the result to the final dataframe
        filtered_rows = pd.concat([filtered_rows, filtered_df], ignore_index=True)

# Save the final filtered dataframe to a new CSV file
filtered_rows.to_csv(output_file, index=False)

print(f"Filtered data has been saved to {output_file}")
