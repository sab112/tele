import requests
from bs4 import BeautifulSoup

class get_price():
 header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

 def __init__(self,price_url):
    self.priceurl = price_url
    
    page = requests.get(self.priceurl, headers=self.header)
    soup = BeautifulSoup(page.content, 'html.parser')

    titel_id = soup.find(id='productTitle')     
    title_text = titel_id.get_text()   
    self.title = title_text.strip()
    print(self.title)

    price_id = soup.find(id='priceblock_ourprice') 
    price_text = price_id.get_text()
    self.price = price_text.replace(',','').lstrip('₹').strip()
    print(self.price)
    price_int = (int(float(price_text.replace(',','').lstrip('₹').strip())))


url = 'https://api.telegram.org/bot1332343561:AAHrYoSJmke-WCrAAmKMS0IN-_BZIazAzFY/getUpdates'
url1 = 'https://api.telegram.org/bot1332343561:AAHrYoSJmke-WCrAAmKMS0IN-_BZIazAzFY/sendMessage'

# group chat bot
prevpost = ''
while True:    
     
    rgetupdates = requests.get(url)
     
    data = rgetupdates.json()
    result = data['result']

    lastid = result[-1:] 
    lastest_updated_id = lastid[0]['update_id']
    
    if len(result) == 100:
       url = url + '?offset=' + str(lastest_updated_id)

  
    if prevpost == lastest_updated_id:
        continue

    lasttext = lastid[0]['message']['text'] 
    print(lastid) 
    print(lasttext)

    if lasttext=='hi':       
        data1 = {"chat_id":"@myjarvisgroup", "text":"hi how are you"}
        rpost = requests.post(url1,data=data1)
    elif lasttext=='im good':
        data1 = {"chat_id":"@myjarvisgroup", "text":"me too"}
        rpost = requests.post(url1,data=data1)    
    elif lasttext=='b':
        data1 = {"chat_id":"@myjarvisgroup", "text":"bye"}
        rpost = requests.post(url1,data=data1)
        break

    if lasttext[:6] == 'https:':
        if 'www.amazon' and '/dp/B0' in lasttext:
            amazon = get_price(lasttext)
            data1 = {"chat_id":"@myjarvisgroup", "text":amazon.title+'\n'+amazon.price}
            rpost = requests.post(url1,data=data1)
        else:
            data1 = {"chat_id":"@myjarvisgroup", "text":'this is not amazon'}
            rpost = requests.post(url1,data=data1)

    prevpost = lastest_updated_id
    print(prevpost)
