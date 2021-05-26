from TikTokApi import TikTokApi

api = TikTokApi.get_instance()

posts = api.by_username("rida1fatima", 1);
for tiktok in posts:
    # Prints the text of the tiktok
    print(tiktok["desc"])
