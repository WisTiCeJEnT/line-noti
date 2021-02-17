import requests
from time import sleep
import datetime
import hashlib
import hmac
import json
import requests
import os

API_HOST = os.getenv('API_HOST')
API_KEY = os.getenv('API_KEY')
API_SECRET = bytes(os.getenv('API_SECRET'), 'utf-8')
url = os.getenv('line_url')
token = os.getenv('line_token')
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
    headers = {'Authorization' : 'Bearer ' + token}
    return requests.post(url, headers=headers, data = payload, files=file)

while True:
    lineNotify(checkPrice())
    sleep(60*60)
