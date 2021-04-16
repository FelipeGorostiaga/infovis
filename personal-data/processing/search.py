import pandas as pd

df = pd.read_json('./data/SearchQueries.json')
df.drop('searchInteractionURIs', axis=1, inplace=True)
df.columns = ['Device', 'Time', 'Query']
for index, row in df.iterrows():
    if row['Device'] == 'IPHONE_ARM64':
        df.at[index, 'Device'] = 'Iphone'
    elif row['Device'] == 'DESKTOP':
        df.at[index, 'Device'] = 'Desktop'

df.to_csv('search.csv', index = False)