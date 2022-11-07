def get_playlist(user_playlists, to_get):
    for playlist in user_playlists:
        if playlist["name"] == to_get:
            return playlist
    return "Error: Could not find playlist"

def get_tracks(spotify, playlist_id, length):
    ret_val = []
    offset = 0
        
    while offset < length:
        tracks = spotify.user_playlist_tracks(playlist_id=playlist_id
        , offset=offset)["items"]
    
        for track in tracks:
            actual_track = track["track"]
            ret_val.append(actual_track)
        offset += 100
    return ret_val