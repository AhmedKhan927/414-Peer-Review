import pandas as pd
#   2  Very good usage on making different python files for different parts of the code. - Ahmed Khan

def load_data(file_path):
    return pd.read_csv(file_path)

file_path = 'data/processed/education_income.csv'
df = load_data(file_path)

print(df.head())