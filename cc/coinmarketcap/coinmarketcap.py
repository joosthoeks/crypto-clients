

import requests


class CoinMarketCap(object):

    def __init__(self, url='https://api.coinmarketcap.com/v2/'):
        self.__url = url
    
    def __request(self, endpoint, params):
        full_url = '%s%s' % (self.__url, endpoint)

        r = requests.get(full_url, params=params)

        response_code = r.status_code
        if response_code != 200:
            raise Exception('Exception response code: %d' % response_code)

        return r.json()

    def get_listings(self):
        return self.__request('listings/', {})

    def get_ticker(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('ticker/', params)

    def get_ticker_id(self, id, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('ticker/%s/' % id, params)

    def get_global(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('global/', params)

