
print('='*90)
print('='*90)
print()
print('                 ____         ______   ______  ---    ---   ____  ')
print(' \            / /     |       |       /      \ |  \  /  |  /      ')
print('  \    /\    /  |-    |       |       |      | |   \/   |  |-      ')
print('   \  /  \  /   |-    |       |       |      | |        |  |-      ')
print('    \/    \/    \____ /______ |_____  \______/ |        |  \____    to the')
print('                                                                          PyPlayList v1.0')
print()
print('='*90)
print('='*90)


playlist = [
    "Don´t let me down",
    "Sick boy",
    "Thunder Clouds",
    "House beach",
    "Taki Taki",
    "Better",
    "Drew love",
    "Sicko mode",
    "Nothing breaks like a heart",
    "When the partys over",
    "Favela",
    "Hope",
    "Promises",
    "Goodbye"
]


selected_music = input(("Qual música deseja escutar: "))

if selected_music in playlist:
    print("Você está ouvindo a {}".format(selected_music))
else:
    print("Música não encontrada.")
    print()
    add_music = input("Gostaria de adcionar {} a PlayList? ".format(selected_music))
    if add_music == 'Yes':
        playlist.append(selected_music)
        print("Música adcionada com sucesso!")
        print(playlist)