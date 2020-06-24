import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def show_tracks(tracks):
    listy = []
    for i, item in enumerate(tracks['items']):
        track = item['track']
        listy.append("   %d %32.32s %s" % (i, track['artists'][0]['name'],
            track['name']))
    return listy

playlists = sp.user_playlists('siddhant_dubey')

while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
        results = sp.playlist(playlist['id'],
                    fields="tracks,next")
        tracks = results['tracks']
        listy = show_tracks(tracks)
        print(listy)
        filething = open('playlists/' + str(i) + '.txt', "w")
        for x in listy:
            filething.write(x)
            filething.write('\n')
        filething.close()
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None