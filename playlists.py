def get_playlist(user_playlists, to_get):
    for playlist in user_playlists:
        if playlist['name'] == to_get:
            return playlist
    return "Error: Could not find playlist"