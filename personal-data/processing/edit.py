import pandas as pd

df = pd.read_csv('streaming.csv')
print(df.head())

rocks = ['classic rock', 'art rock', 'album rock', 'dance rock', 'british invasion',
'glam rock', 'acid rock', 'adult standards', 'garage rock']

for index, row in df.iterrows():
    genre = row['Genre']
    if genre in rocks:
         df.at[index, 'Genre'] = 'rock'

print(df.head(10))

df.to_csv('streaming-final.csv', index=False)
