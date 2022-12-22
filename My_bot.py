import requests
from pprint import pprint
TOKEN="5939996534:AAEy5kDWYrek1okDGpzuBaLG5pS7ErtcPDo"
def get_updates(TOKEN):
    respose=requests.get(f"https://api.telegram.org/bot{TOKEN}/getUpdates")

    if respose.status_code==200:
        data=respose.json()
        updates=data["result"][-1]["message"]
        chat_id=updates["chat"]["id"]
        text=updates["text"]
        message_id=updates["message_id"]
        return chat_id,text,message_id
        
def send_message(TOKEN,chat_id,text):
    data = {
            'chat_id':chat_id,
            'text':text
        }

    r = requests.post(url = f'https://api.telegram.org/bot{TOKEN}/sendMessage',params=data)    

new_message = -1

while True:
    updates = get_updates(TOKEN)
    
    id,text,last_message_id = updates

    if new_message != last_message_id:
        send_message(TOKEN,chat_id=id,text=text)
        new_message = last_message_id