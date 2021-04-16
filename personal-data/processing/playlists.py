import json
import pandas as pd

file = open('./data/Playlists.json', 'r', encoding="utf8")
data = json.loads(file.read())
playlists = data['playlists']

# Create empty data frame
df = pd.DataFrame(columns=['trackName', 'artistName', 'albumName', 'playlist'])

# Populate dataframe from json object
for playlist in playlists:

    name = playlist['name']
    items = playlist['items']

    for item in items:
        track_detail = item['track']
        track_detail['playlist'] = name
        df = df.append(track_detail, ignore_index = True)

df.columns = ['track', 'artist', 'album', 'playlist']
playlist_names = df['playlist'].value_counts().index.tolist() 
count = len(playlist_names)
print(count)
print(f'You have {count} playlists:')
print(playlist_names)

df.to_csv('playlists.csv', index = False)