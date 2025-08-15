def make_album():
    print()
    print("Bạn có thể nhập \"quit\" tại các câu hỏi để thoát.")
    print("----------------------------------------------------")
    album_info = {}

    while True:
        artist = input("Nghệ sĩ bạn ưa thích là ai?: ")
        if artist.lower() == "quit":
            break

        album = input("Album bạn ưa thích của người nghệ sĩ đó?: ")
        if album.lower() == "quit":
            break

        album_info[artist] = album
        
    for k, v in album_info.items():
        print(f"{k}: {v}")


make_album()

