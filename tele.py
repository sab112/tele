import requests
from datetime import datetime
url = 'https://api.telegram.org/bot1332343561:AAHrYoSJmke-WCrAAmKMS0IN-_BZIazAzFY/sendMessage'
m = [7]
tempt = 0
while True:    
        t1 = datetime.now()
        if t1.minute in m and tempt != t1.minute:
                data1 = {"chat_id":"@myjarvisgroup", "text":f"{t1}   -heroku"}
                rpost = requests.post(url,data=data1)
                tempt = t1.minute
                

