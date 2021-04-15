import pandas as pd
import requests
import base64
import json

# TODO: get from .env file
spotify_base_address =  'https://api.spotify.com.'
client_id =  '977f73bb16a84406b785e8fd3d66be02'
client_secret = 'd8100158832a47079e45c9b91a91fbb0' 

# Streaming History 
""" df_s0 = pd.read_json('./data/StreamingHistory0.json')
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

df.to_csv('streaming.csv', index = False) """

client_credentials = f'{client_id}:{client_secret}'
creds_64 = base64.b64encode(client_credentials.encode())
auth_url = 'https://accounts.spotify.com/api/token'
auth_method = 'POST'
token_data = {
    'grant_type': 'client_credentials'
}
token_headers = {
    'Authorization': f'Basic {creds_64.decode()}' 
}
# Make request to Spotify API to get track genre

r = requests.post(auth_url, data=token_data, headers=token_headers)
response_data = r.json()
access_token = response_data['access_token']
expires_in = response_data['expires_in']
print(access_token)
