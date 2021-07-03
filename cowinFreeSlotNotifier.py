import requests,json
from configparser import ConfigParser
from datetime import datetime
import os
import telebot,logging

devKeys = os.environ.get('DevKeys')
config = ConfigParser()
config.read(devKeys)

telegramToken=config['telegram']['accessToken']
tb = telebot.TeleBot(telegramToken)

logfilename = os.path.join(os.getcwd(),'logs.txt')
logging.basicConfig(filename=logfilename,format='%(asctime)s %(message)s',level=logging.INFO)


ChatIds= {
    "NotifierSpace1":"1458048263"
}

def sendTelegramMessage(message):
    for space in ChatIds.keys():
        tb.send_message(ChatIds[space], message)


headers = {
    'authority': 'cdn-api.co-vin.in',
    'cache-control': 'no-cache',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'origin': 'https://www.cowin.gov.in',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.cowin.gov.in/',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'
}

bangaloreCenters = {
    "BBMP":'294',
    "Bangalore Urban":'265',
    "Bangalore Rural":'276'
}

totalSlots = 0
message = ''
for keys in bangaloreCenters.keys():
    params = {}
    params['district_id'] = bangaloreCenters[keys]
    today = datetime.today()
    date = today.strftime("%d-%m-%Y")
    params['date'] = date
    
    districtUrl = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict'
    response = requests.get(districtUrl, headers=headers, params=params)
    bbmp_json = json.loads(response.content)
    for center in bbmp_json['centers']:
        if 'vaccine_fees' not in center:
            vaccineAvailable = False
            available_capacity = 0
            for session in center['sessions']:
                if session['min_age_limit'] == 18 and session['available_capacity'] > 5:
                    vaccineAvailable = True
                    available_capacity = available_capacity + session['available_capacity']
                    totalSlots =  totalSlots + session['available_capacity']
            if vaccineAvailable:
                message = message + '\n\n' + center['name'] + '(' + str(center['pincode']) + ')' + '-' + str(available_capacity)
                print(center['name'],'(',center['pincode'],')-',available_capacity)
    if message != '':
        sendTelegramMessage(message)
    else:
        logging.info("Currently No Free Vaccines Available")

print("Total Free Slots:",totalSlots)