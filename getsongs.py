import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

bellion_uri = 'spotify:artist:50JJSqHUf2RQ9xsHs0KMHg'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.artist_albums(bellion_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])


songs = []
for album in albums:
    tracks = []
    results = spotify.album_tracks(album['id'])
    tracks.extend(results['items'])
    while results['next']:
        results = spotify.next(results)
        tracks.extend(results['items'])
    for track in tracks:
        songs.append(track['name'])
songs = list(dict.fromkeys(songs))
filey = open('songs.txt', "w+")
for song in songs:
    filey.write(song)
    filey.write('\n')
filey.close()