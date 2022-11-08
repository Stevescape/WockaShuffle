import random

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

def categorize(tracks):
    ret_val = {}
    for track in tracks:
        artist = track["artists"][0]["name"]
        if artist not in ret_val.keys():
            ret_val[artist] = set()
        ret_val[artist].add((track["name"], track["id"], artist))
    return ret_val

def shuffle_tracks(tracks_dict, playlist_length):
    '''
    Will shuffle with the intent of spreading out tracks by the same artist

    tracks_dict = {artist: array of tracks by artist}
    playlist_length = total amount of tracks in playlist/dictionary
    '''
    track_list = {}
    for artist, tracks in tracks_dict.items():
        # Tracks is a set of tuples (track_name, track_id)
        max_disparity = round(playlist_length/len(tracks))
        min_disparity = max_disparity - 5
        while min_disparity >= max_disparity:
            min_disparity -= 1
        if min_disparity < 0:
            min_disparity = 0

        first_run = True

        # We loop through all the tracks starting from index 1 onwards skipping
        # the first track
        cur = None
        for track in tracks:
            if first_run:
                 # The first track must be handled differently
                 
                 # Place the first song at the start of the queue
                cur = random.randint(0, round(playlist_length/10))
                if cur not in track_list.keys():
                    track_list[cur] = set()
                track_list[cur].add(track)
                first_run = False
            else:
                cur += random.randint(min_disparity, max_disparity)
                if cur not in track_list.keys():
                    track_list[cur] = set()
                track_list[cur].add(track)
    
    combined_track = []
    for i in sorted(track_list.keys()):
        tracks_to_add = track_list[i]
        for track in tracks_to_add:
            combined_track.append(track)
    return combined_track

def create_playlist(spotify, user, track_list):
    shuffled_playlist = spotify.user_playlist_create(user, "WockaShuffle Playlist", public=False,
                                                    description="Shuffled Playlist")
    for i in shuffled_playlist:
        print(i)
            