def make_album(artist_name, album_title, songs= None):
    album = {"artist": artist_name, "title": album_title}
    if songs is not None:
        album['songs'] = songs
    
    return album

print(make_album("Taylor Swift", "1989"))
print(make_album("Adele", "25"))
print(make_album("Ed Sheeran", "Divide", 16))