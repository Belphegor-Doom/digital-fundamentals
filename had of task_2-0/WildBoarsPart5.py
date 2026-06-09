import pandas as pd
df = pd.read_csv('wild_boars.csv')
grouped_std = df.groupby('gender')['tusk_length_cm'].std()
grouped_mean = df.groupby('gender')['tusk_length_cm'].mean()
cv_tusks = (grouped_std / grouped_mean) * 100
cv_df = cv_tusks.reset_index(name='coefficient_of_variation_%')
cv_df.to_csv('tusk_cv.csv')