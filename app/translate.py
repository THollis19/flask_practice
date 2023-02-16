import json
import requests
from flask_babel import _
from app import app

def translate (text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or not app.config['MS_TRANSLATOR_KEY']:
        return ('Error: the translation service is not configured')
    auth = {
        'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY'],
        'Ocp-Apim-Subscription-Region': 'eastus'
    }
    print('sending request')
    print('https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from={}&to={}'.format(source_language, dest_language))
    print(auth)
    print(text)

    r = requests.post('https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from={}&to={}'.format(source_language, dest_language), headers=auth, json=[{'Text': text}])
    if r.status_code != 200:
        print(r.status_code)
        print(r.reason)
        print(r.headers)
        return ('Error: the translation service failed.')
    print(r.status_code)
    print(r.json()[0]['translations'][0]['text'])
    return r.json()[0]['translations'][0]['text']