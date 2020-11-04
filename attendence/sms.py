import requests 
import json
def send():
    url = "https://www.fast2sms.com/dev/bulk"
    # f = open("data.txt",'r')
    number = 'hello'
    apikey = ''
    

    my_data = {'sender_id': 'FSTSMS',
               'message': 'Looks like your attendance link is posted!!',
               'language': 'english',
               'route': 'p',
               'numbers': number}

    headers = { 
	'authorization': apikey, 
	'Content-Type': "application/x-www-form-urlencoded", 
	'Cache-Control': "no-cache"}

    requests.request("POST",url,data = my_data,headers = headers)
    # returned_msg = json.loads(response.text)
    # print(returned_msg['message'])

# sms()