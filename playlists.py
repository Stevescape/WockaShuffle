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
            track_id = actual_track["id"]
            track_name = actual_track["name"]
            ret_val.append(track_id)
        offset += 100
    return ret_val