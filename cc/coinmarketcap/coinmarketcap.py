

import requests


class CoinMarketCap(object):

    def __init__(self, url):
        self.__url = url
    
    def __request(self, path, params):
        full_path = '%s%s' % (self.__url, path)

        r = requests.get(full_path, params=params)

        response_code = r.status_code
        if response_code != 200:
            raise Exception('Exception response code: %d' % response_code)

        return r.json()

    def get_ticker(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('ticker', params)

    def get_ticker_id(self, id, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('ticker/%s' % id, params)

    def get_global(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('global', params)

