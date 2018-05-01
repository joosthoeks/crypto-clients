

import requests
import urllib.parse


class Bitstamp(object):

    def __init__(self, url='https://www.bitstamp.net/api/v2/'):
        self.__url = url
    
    def __request(self, endpoint, params):
        full_url = '%s%s' % (self.__url, endpoint)
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
    
