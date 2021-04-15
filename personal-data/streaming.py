import pandas as pd

# Streaming History 
df_s0 = pd.read_json('./data/StreamingHistory0.json')
df_s1 = pd.read_json('./data/StreamingHistory1.json')
df_s2 = pd.read_json('./data/StreamingHistory2.json')

df = pd.concat([pd.concat([df_s0,df_s1]), df_s2])
df['msPlayed'] = df['msPlayed'].apply(lambda x: float(x / 60000))
df.columns = ['Date', 'Artist', 'Track', 'MinPlayed']

track_count = len(df['Track'].value_counts())  
top_tracks = df['Track'].value_counts()[:6].index.tolist()
top_artists = df['Artist'].value_counts()[:6].index.tolist()

print(f'Track count: {track_count}')
print(f'Most listened track: {top_tracks}')
print(f'Most listened artist: {top_artists}')

df.to_csv('streaming.csv', index = False)