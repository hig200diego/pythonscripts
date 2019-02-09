playlist = {'title': 'Pop songs 2019', 
            'author': 'Diego Freire',
           'songs': [
               {'title': 'Let Me Down Slowly', 'artist': ['Alec Benjamin'], 'duration': 2.57 },
               {'title': 'Thank u, next', 'artist': ['Ariana Grande'], 'duration': 5.30 },
               {'title': 'Favela', 'artist': ['Ina Wroldsen, Alok'], 'duration': 3.4 },
               {'title': 'LSD-Thunderclouds', 'artist': ['Sia, Diplo,...'], 'duration': 3.15 }
           ]}

for song in  playlist['songs']:
    print(song['artist'])
    
total_length = 0 #começa com um valor zer0
for song in playlist['songs']: #loop atraves do item songs
    total_length += song['duration']
print(total_length)

