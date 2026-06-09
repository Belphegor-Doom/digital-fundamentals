import pandas as pd
df = pd.read_csv('wild_boars.csv')
print(df['tusk_length'])
print(df['tusk_length'].min())
print(df['tusk_length'].max())