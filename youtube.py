from pyyoutube import Api

api = Api(api_key="AIzaSyBjkPWhH-pTk-MiWaTl1iZBCiyVaLJw5Co")
channel_by_id = api.get_channel_info(channel_id="UCfpjCLOmLadxkc_eoOzuybg")
playlist_id = channel_by_id.items[0].contentDetails.relatedPlaylists.uploads
print(playlist_id)
playlist = api.get_playlist_by_id(playlist_id=playlist_id).items[0]
print(playlist)
playlist_item_by_playlist = api.get_playlist_items(playlist_id=playlist_id, count=2)
video = playlist_item_by_playlist.items[0].snippet.resourceId.videoId
print(video)