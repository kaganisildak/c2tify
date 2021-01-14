import spotify
import encoder

#spotify:playlist:7pcXAz0de0NgQ6Q05okOnb


extracted = ""
offset = 0

while True:
    tracks = spotify.get_tracks("7pcXAz0de0NgQ6Q05okOnb",offset=offset)["items"]
    if len(tracks) == 0:
        break
    for track in tracks:
        extracted +=track["track"]["name"][0]
    offset = offset + len(tracks)

open("ext.zip","wb").write(encoder.base32_decode(extracted))