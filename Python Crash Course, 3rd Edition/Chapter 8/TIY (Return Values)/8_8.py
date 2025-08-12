def make_album(artist_name, title, nums_song= None):
    album = {"artist" : artist_name,
             "title" : title}
    if nums_song is not None:
        album['song'] = nums_song
    return album

while True:
    fav_artist = input("Enter your favorite artist: ")
    fav_album = input("Enter your favorite album by that artist: ")
    fav_song = input("Enter your favorite song from that album.If you don't have one, enter 'q':")
    if fav_album == 'q':
        full = make_album(fav_artist, fav_album)
        print(full)
    else:
        full = make_album(fav_artist, fav_album, fav_song)
        print(full)
    print('='*50)
        