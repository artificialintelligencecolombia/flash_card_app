import pandas as pd
import re

# Define the file path
FILE_PATH = './data/raw_data_ru.csv'

# Load de raw CSV file + without a header
df = pd.read_csv(FILE_PATH, header=None)
# print("\nOriginal File: \n")
# print(df)

# Define the header and add it to the DataFrame
header_list = ['russian']
df.columns = header_list

# Remove numbers and extra spaces
df['russian'] = df['russian'].apply(lambda x: re.
                                      sub(r'\d+','',x).strip())

# Save cleaned data
df.to_excel('./data/cleaned_data.xlsx', index=False, sheet_name="traslator")

# Testing
#df_modii = pd.read_csv('./data/cleaned_data.csv')
#print(df_modii)