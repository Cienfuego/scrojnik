import json
import requests
from flask import current_app
from flask_babel import _


#def translate(text, source_language, dest_language):
#    if 'MS_TRANSLATOR_KEY' not in current_app.config or \
#            not current_app.config['MS_TRANSLATOR_KEY']:
#        return _('Error: the translation service is not configured.')
#    auth = {
#        'Ocp-Apim-Subscription-Key': current_app.config['MS_TRANSLATOR_KEY']}
#    r = requests.get('https://api.microsofttranslator.com/v2/Ajax.svc'
#                     '/Translate?text={}&from={}&to={}'.format(
#                         text, source_language, dest_language),
#                     headers=auth)
#    if r.status_code != 200:
#        return _('Error: the translation service failed.')
#    return json.loads(r.content.decode('utf-8-sig'))

def translate(text, source_language, dest_language):
    auth = current_app.config['YD_TRANSLATOR_KEY']
    lang = source_language +'-'+ dest_language
    r = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate?key={}&text={}&lang={}'.format(auth, text, lang))
    #if r.status_code != 200:
    #    return _('Error: the translation service failed.')
    #y = json.loads(r.content.decode('utf-8-sig'))
    #ytext = y["text"]
    #return ytext[0]

    return json.loads(r.content.decode('utf-8-sig'))["text"]
    #return y[0]

