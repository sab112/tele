import requests
from bs4 import BeautifulSoup

url = 'https://api.telegram.org/bot1332343561:AAHrYoSJmke-WCrAAmKMS0IN-_BZIazAzFY/sendMessage'

while True:    
        data1 = {"chat_id":"@myjarvisgroup", "text":"hi how are you -heroku"}
        rpost = requests.post(url1,data=data1)

