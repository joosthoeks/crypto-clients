

import requests


class Binance(object):

    def __init__(self, url='https://api.binance.com/api/'):
        self.__url = url

    def __request(self, endpoint, params, method='GET', credential=None):
        full_url = '%s%s' % (self.__url, endpoint)
        if credential is None:
            r = requests.get(full_url, params=params)
        response_code = r.status_code
        if response_code != 200:
            raise Exception('Exception response code: %d' % response_code)
        return r.json()

    # General endpoints:
    def ping(self):
        return self.__request('v1/ping', {})

    def time(self):
        return self.__request('v1/time', {})

    def exchange_info(self):
        return self.__request('v1/exchangeInfo', {})

    # Market Data endpoints:
    def depth(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('v1/depth', params)

    def trades(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('v1/trades', params)

    def agg_trades(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('v1/aggTrades', params)

    def klines(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('v1/klines', params)

    def ticker_24hr(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('v1/ticker/24hr', params)

    def ticker_price(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('v3/ticker/price', params)

    def ticker_book_ticker(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('v3/ticker/bookTicker', params)

    # TODO Account endpoints:

