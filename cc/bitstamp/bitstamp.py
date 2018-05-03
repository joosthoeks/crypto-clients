

import requests
import urllib.parse
import time
import hmac
import hashlib


class Bitstamp(object):

    def __init__(self, url='https://www.bitstamp.net/api/v2/'):
        self.__url = url
    
    def set_credential(self, customer_id, pub_key, sec_key):
        self.__customer_id = customer_id
        self.__pub_key = pub_key
        self.__sec_key = sec_key
    
    def __get_credential(self):
        nonce = int(time.time())
        message = nonce + self.__customer_id + self.__pub_key
        signature = hmac.new(
                self.__sec_key,
                msg=message,
                digestmod=hashlib.sha256
                ).hexdigist().upper()
        return nonce, signature

    def __request(self, endpoint, params, credential=False):
        full_url = '%s%s' % (self.__url, endpoint)
        if credential:
            nonce, signature = self.__get_credential()
            # TODO
            r = requests.post(full_url, data=params)
        else:
            r = requests.get(full_url, params=params)
        response_code = r.status_code
        if response_code != 200:
            raise Exception('Exception response code: %d' % response_code)
        return r.json()

    # Public data functions:
    def ticker(self, market):
        return self.__request('ticker/%s/' % market, {})

    def ticker_hour(self, market):
        return self.__request('ticker_hour/%s/' % market, {})
    
    def order_book(self, market):
        return self.__request('order_book/%s/' % market, {})

    def transactions(self, market, time='hour'):
        params = {'time': time}
        return self.__request('transactions/%s/' % market, params)

    def trading_pairs_info(self):
        return self.__request('trading-pairs-info/', {})

    # TODO Private functions:
    
