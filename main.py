import requests
import time
import datetime
from instascrape import *
# from selenium.webdriver import Chrome 


profiles = ["https://www.instagram.com/irfanjunejo/", "https://www.instagram.com/ganjiswag/", "https://www.instagram.com/mooroosicity/", "https://www.instagram.com/alinahxyat/"]
sessionid = "sessionid=391635289%3AKJPeOsoTgKlp08%3A16;"
headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57",
    "cookie": sessionid
}
# webdriver = Chrome("C:/Users/moiz_/Downloads/chromedriver.exe")

while True:
    for profile in profiles:
        creator = Profile(profile)
        creator.scrape(headers=headers)
        print(datetime.datetime.now())
        print(creator.username)
        print(creator.followers)
        posts = creator.get_recent_posts(1)
        print(posts[0].display_url)
        print(str(posts[0].caption))
        print("\n");
        time.sleep(300)