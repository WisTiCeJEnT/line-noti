import requests
from time import sleep
import datetime
import hashlib
import hmac
import json
import requests

API_HOST = 'https://api.bitkub.com'
API_KEY = '8a0b8f4649d9c8c4858181ee286c6714'
API_SECRET = b'c4e815924288b34c32d942a4cb29a624'

mycoins = ['THB_ADA']

def checkPrice():
	response = requests.get(API_HOST + '/api/market/ticker')
	result = response.json()
	alltext = ''
	sym = 'THB_ADA'
	data = result[sym]
	last = data['last']
	return sym + ': ' + str(last)
  
def lineNotify(message):
    payload = {'message' : message}
    return _lineNotify(payload)

def _lineNotify(payload, file=None):
    url = 'https://notify-api.line.me/api/notify'
    token = 'ceE0ixKWTLi74RRj8mDgEIMkv6wIVXJd2QngytIruJU'
    headers = {'Authorization' : 'Bearer ' + token}
    return requests.post(url, headers=headers, data = payload, files=file)

while True:
    lineNotify(checkPrice())
    sleep(60)
