

import requests
import urllib.parse


class Bitstamp(object):

    def __init__(self, url='https://www.bitstamp.net/api/v2/'):
        self.__url = url

