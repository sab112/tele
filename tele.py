import requests
from time import *

url = 'https://api.telegram.org/bot1332343561:AAHrYoSJmke-WCrAAmKMS0IN-_BZIazAzFY/sendMessage'
i=0
while True:    
        i += 1
        txt = f'{i}) every 1 hour   -heroku'
        data1 = {"chat_id":"@myjarvisgroup", "text":txt}
        rpost = requests.post(url,data=data1)      
        sleep(60 * 60)
         
                

