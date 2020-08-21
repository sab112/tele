import requests
from datetime import datetime
url = 'https://api.telegram.org/bot1332343561:AAHrYoSJmke-WCrAAmKMS0IN-_BZIazAzFY/sendMessage'
while True:    
        t1 = datetime.now()
        if t1.minute == 51 
                data1 = {"chat_id":"@myjarvisgroup", "text":"hi how are you -heroku"}
                rpost = requests.post(url,data=data1)

