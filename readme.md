### Features
- Notifies the Free Vaccination Slots Available to Telegram.
- You can update the district id of your choice and get notified.
- This code can be used to run in your servers to notify the slots available to your Telegram

## Telegram Bot 
### Create Telegram Bot
Unlike Whatsapp Bot, Telegram Bots are free to use. Telegram Bot are widely used by several developers to build applications. First you need to have a Telegram Account and bot can be registered by following the [link](https://sendpulse.com/knowledge-base/chatbot/create-telegram-chatbot)

### Copy the Telegram Token
Copy the Telegram Access Token in to a credentials file. The telegram access token looks like this
```
[telegram]
accessToken = 1891112227:AAHdsasd&askjlasMIya6ppKGu9lAKluiMtkwdSsiZdx_f0
```

### Export the Location of creds File into environment variable
To avoid access tokens being shared, I follow this apporach of having the path to credentials file stored in a environment variable
```
export DevKeys=/Users/Achuth/Keys/cred
```

### Get the Chat Id of the Space
Get the chat Id of the space you want to ping the notifications to and copy the chat id to the chatIds dictionary.
```
ChatIds= {
    "NotifierSpace1":"1458048263"
}
```

### Get the District Ids
I have implemented this script for the Bangalore Urban,Rural and BBMP. You can modify the script to your needs by adding the Disrict IDs of your choice.  Refer more to APIs at [APISetu](https://apisetu.gov.in/public/api/cowin)

Get the List of All State IDs
```
https://cdn-api.co-vin.in/api/v2/admin/location/states
```
Get the District Ids
```
https://cdn-api.co-vin.in/api/v2/admin/location/districts/16
```
Change the District Ids in the script if needed.
```
bangaloreCenters = {
    "BBMP":'294',
    "Bangalore Urban":'265',
    "Bangalore Rural":'276'
}
```

## Installations and Dependencies
```
$ pip3 install -r requirements.txt
```

## How to run the Script ?
```
$ python3 cowinFreeSlotNotifier.py
```