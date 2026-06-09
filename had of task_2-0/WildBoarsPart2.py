import pandas as pd
df = pd.read_csv('wild_boars.csv')
average_lenght = df['tusk_lenght'].mean()
print(f"Boars average tusk length is {average_lenght:.2f} sm")