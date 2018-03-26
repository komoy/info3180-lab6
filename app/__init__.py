from flask import Flask
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='5a774af36fda4099ae1fe29329b57b94')

app = Flask(__name__)
from app import views