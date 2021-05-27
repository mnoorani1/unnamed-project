from pyyoutube import Api

creators = ["UCI9tIvSPsdxNEICjZk7ujUA", "UCfpjCLOmLadxkc_eoOzuybg", "UCQ2P7C8UGoVM6AhqsVx-M0Q", "UCuqBZWK9Wrol_4Y22DzisFQ", "UCn68MHKSGluDcSQbABxW4EQ", "UCQexaAjPn3-1MCE4DmBK3Tg", "UCqhQRA_Y8Lyu5BYnFOpvtAQ", "UC_c-RTowPbIlzMkIa_O7s6Q",
"UCaDnOdsVpL98eDF9R3cVejw", "UCTqMx8l2TtdZ7_1A40qrFiQ", "UCw5z1bEMXv7uVyQ0gZ5VVJg", "UCTuOFKW8PpQ3p499XYyGXTA", "UCheoCqHDwPcfS9Jrgz8siQw", "UCKNZhH_PzvCMBMKPd542rsQ", "UCBqUbOUyAsTB7Xc7xQAHWZA", "UCTsP4f7LoJG4SJPF0qER_xg",
"UCUuDUW0Y6IQZYDvH1QQBsgA", "UC3nzFvADzctm2hdQYrSurgg", "UCaJlGhCNsdqS_t8FbiOVREg", "UC-rP-oFlxQGpSLYHBlhIWkg"]
api = Api(api_key="")
channel_by_id = api.get_channel_info(channel_id="UCfpjCLOmLadxkc_eoOzuybg")
playlist_id = channel_by_id.items[0].contentDetails.relatedPlaylists.uploads
print(playlist_id)
playlist = api.get_playlist_by_id(playlist_id=playlist_id).items[0]
print(playlist)
playlist_item_by_playlist = api.get_playlist_items(playlist_id=playlist_id, count=2)
video = playlist_item_by_playlist.items[0].snippet.resourceId.videoId
print(video)
