import pandas as pd
df = pd.read_csv('wild_boars.csv')
median_length = df['tusk_length'].median()
print(f"Boars median tusk length is {median_length:.2f}")