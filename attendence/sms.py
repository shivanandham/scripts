import requests 
import json
def send():
    url = "https://www.fast2sms.com/dev/bulk"
    # f = open("data.txt",'r')
    global number = '8610171639'
    global apikey = 'taqIFWfpBGYrQxN81ie029wXP4uRKCsTVbUH6Ek3jlAgMDZO7nkl4a3KWVOXm5PyS0CYtHF7IzEhfobU'
    

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