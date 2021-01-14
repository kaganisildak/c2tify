import encoder
import spotify


target_file = encoder.base32_encode(encoder.get_file("stub.zip"))


print(target_file)
playlist = spotify.create_playlist("c2")

for a in target_file:
    track_id = spotify.track_finder(a)[1]
    print(track_id)
    spotify.add_to_playlist(playlist["id"],track_id)