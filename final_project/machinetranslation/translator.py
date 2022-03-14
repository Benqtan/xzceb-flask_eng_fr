"""System module."""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishtofrench(englishtext):
    """English to french translation"""
    text = language_translator.translate(text=englishtext, model_id='en-fr').get_result()
    frenchtext = text['translations'][0]['translation']
    return frenchtext

def frenchtoenglish(frenchtext):
    """French to english translation"""
    text = language_translator.translate(text=frenchtext, model_id='fr-en').get_result()
    englishtext = text['translations'][0]['translation']
    return englishtext
