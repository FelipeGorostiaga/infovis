import requests
import base64
import json

client_id = 'clientId'
client_secret = 'clientSecret'
auth_url = 'https://accounts.spotify.com/api/token'
search_url = 'https://api.spotify.com/v1/search'

def get_access_token():
    client_credentials = f'{client_id}:{client_secret}'
    creds_64 = base64.b64encode(client_credentials.encode())
    token_data = {
        'grant_type': 'client_credentials'
    }
    token_headers = {
        'Authorization': f'Basic {creds_64.decode()}'
    }
    r = requests.post(auth_url, data=token_data, headers=token_headers)
    response_data = r.json()
    return response_data['access_token']

def get_artist_genre(artist, access_token):
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    params = {
        'q': artist,
        'type': 'artist'
    }
    r = requests.get(search_url, params=params, headers=headers)

    if (r.status_code not in range(200,299)):
        return "N/A"

    data = r.json()   
    try:
        genre = data['artists']['items'][0]['genres'][0]
        return genre
    except:
        return 'N/A'
    