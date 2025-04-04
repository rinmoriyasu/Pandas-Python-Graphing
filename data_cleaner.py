import pandas as pd

filename = 'light_crude_sara_data.csv'
file = filename.replace(".csv", "")
data = pd.read_csv(filename)
data_cleaned = data.dropna(how='any') #This removes rows with NaN or empty string values

data_cleaned.to_csv(f'cleaned_{file}.csv', index=False)