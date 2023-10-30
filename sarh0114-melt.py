import pandas as pd
import numpy as np

# Specify the path to the 'sarh0114-result.csv' file
csv_file_path = 'sarh0114-result.csv'

# Load the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Specify the columns to keep as identifier variables
id_vars = ['Year', 'Quarter', 'Tasking Location Type', 'Period']

# Specify the columns to melt (location-specific columns)
value_vars = ['Caernarfon', 'Humberside', 'Inverness', 'Lee On Solent', 'Lydd', 'Newquay', 'Portland', 'Prestwick', 'St Athan', 'Stornoway', 'Sumburgh', 'Total']

# Use the melt function to reshape the DataFrame
melted_df = pd.melt(df, id_vars=id_vars, value_vars=value_vars, var_name='Location', value_name='Value')

# Define the ONS Geography code mapping
ons_code_mapping = {
    'Caernarfon': 'E123456',
    'Humberside': 'E234567',
    'Inverness': 'E345678',
    'Lee On Solent': 'E456789',
    'Lydd': 'E567890',
    'Newquay': 'E678901',
    'Portland': 'E789012',
    'Prestwick': 'E890123',
    'St Athan': 'E901234',
    'Stornoway': 'E012345',
    'Sumburgh': 'E123456'
}

# Add the 'ONScode' column based on the mapping
melted_df['ONScode'] = melted_df['Location'].map(ons_code_mapping)

# Replace ':' with NaN in the 'Value' column and update 'obsStatus'
melted_df['Value'] = melted_df['Value'].replace(':', np.nan)
melted_df['obsStatus'] = melted_df['Value'].apply(lambda x: 'x' if pd.isna(x) else '')

# Reorder the columns to place 'ONScode' after 'Location'
new_column_order = ['Year', 'Quarter', 'Tasking Location Type', 'Period', 'Location', 'ONScode', 'Value', 'obsStatus']
melted_df = melted_df[new_column_order]

# Reset the DataFrame index
melted_df = melted_df.reset_index(drop=True)

# Save the melted DataFrame to a new CSV file
result_csv_path = 'melted_sarh0114-result.csv'
melted_df.to_csv(result_csv_path, index=False)

print(f'Melted DataFrame saved to "{result_csv_path}"')
