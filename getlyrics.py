import lyricsgenius
genius = lyricsgenius.Genius("zfkZRZwpWAI8xfaDdZZEH3CHQ7CIjfAyvjxH4FHyNU-Tsb6HNZf2p9G1cE5y_V9G")
f = open("songs.txt", "r+")

song_names = []
for line in f: 
    song_names.append(line)
f.close()
songs = []
for song in song_names:
    songx = song.rstrip()
    songy = songx.strip()
    songs.append(songy)
for s in songs:
    f = open("lyrics/" + str(s) + ".txt", "w+")
    song = genius.search_song(s)
    if song is None:
        pass
    else:
        f.write(song.lyrics)
