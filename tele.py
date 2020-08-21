import requests
from time import *

url = 'https://api.telegram.org/bot1332343561:AAHrYoSJmke-WCrAAmKMS0IN-_BZIazAzFY/sendMessage'

while True:    
        data1 = {"chat_id":"@myjarvisgroup", "text":"every 1 hour   -heroku"}
        rpost = requests.post(url,data=data1)      
        sleep(60 * 60)
         
                

