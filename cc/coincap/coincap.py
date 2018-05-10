

import requests


class CoinCap(object):
    
    def __init__(self, url='http://coincap.io/'):
        self.__url = url

    def __request(self, endpoint, params):
        full_url = '%s%s' % (self.__url, endpoint)

        r = requests.get(full_url, params=params)

        response_code = r.status_code
        if response_code != 200:
            raise Exception('Exception response code: %d' % response_code)

        return r.json()

    def get_coins(self):
        return self.__request('coins/', {})

    def get_map(self):
        return self.__request('map/', {})

    def get_front(self):
        return self.__request('front/', {})

    def get_global(self):
        return self.__request('global/', {})

    def get_page(self, coin):
        return self.__request('page/%s/' % coin, {})

    def get_history(self, coin):
        return self.__request('history/%s/' % coin, {})

    def get_history_1day(self, coin):
        return self.__request('history/1day/%s/' % coin, {})

    def get_history_7day(self, coin):
        return self.__request('history/7day/%s/' % coin, {})

    def get_history_30day(self, coin):
        return self.__request('history/30day/%s/' % coin, {})

    def get_history_90day(self, coin):
        return self.__request('history/90day/%s/' % coin, {})

    def get_history_180day(self, coin):
        return self.__request('history/180day/%s/' % coin, {})

    def get_history_365day(self, coin):
        return self.__request('history/365day/%s/' % coin, {})


