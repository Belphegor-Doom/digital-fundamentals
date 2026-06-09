import pandas as pd
df = pd.read_csv('wild_boars.csv')
mode_length = df['tusk_length'].mode()
print(f"Boars median tusk length is {mode_length:.2f}")