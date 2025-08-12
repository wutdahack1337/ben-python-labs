def make_album(artist_name, title, nums_song= None):
    album = {"artist" : artist_name,
             "title" : title}
    if nums_song is not None:
        album['song'] = nums_song
    return album

album1 = make_album('Taylor Swift', '1989')
album2 = make_album('Adele', '25')
album3 = make_album('Ed Sheeran', 'Divide', 12)

print()

print(album1)
print("-"*60)
print(album2)
print("-"*60)
print(album3)