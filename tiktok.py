from TikTokApi import TikTokApi

api = TikTokApi.get_instance()
creators = ["rida1fatima", "mjahsan20", "reejajeelani", "pirahmed", "mubeenrehman66", "anumasad", "hussain.yasir", "noorhassan17", "jannatmirza", "phoolllu", "ch.zulqarnain25", "usmanasim66", "hareemshahofficialx",
"sundalkhattakofficial", "aalleey", "ibrahimo33", "alishbahanjum", "areeka__haq", "pinkyfrancis", "sehar_hayyat"]
posts = api.by_username("rida1fatima", 1);
for tiktok in posts:
    # Prints the text of the tiktok
    print(tiktok["desc"])
