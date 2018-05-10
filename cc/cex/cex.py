

import requests


class Cex(object):
    def __init__(self, url='https://cex.io/api/'):
        self.__url = url

    def __request(self, endpoint, params, method='GET', credential=False):
        full_url = '%s%s' % (self.__url, endpoint)
        if credential:
            '''
            '''
        else:
            if method is 'GET':
                r = requests.get(full_url, params=params)
            if method is 'POST':
                r = requests.post(full_url, data=params)
        response_code = r.status_code
        if response_code != 200:
            raise Exception('Exception response code: %d' % response_code)
        return r.json()

    # Public API calls:
    def currency_limits(self):
        return self.__request('currency_limits/', {})

    def ticker(self, symbol1, symbol2):
        return self.__request('ticker/%s/%s/' % (symbol1, symbol2), {})

    def tickers(self, symbol1, symbol2):
        return self.__request('tickers/%s/%s/' % (symbol1, symbol2), {})

    def last_price(self, symbol1, symbol2):
        return self.__request('last_price/%s/%s/' % (symbol1, symbol2), {})

    def last_prices(self, symbol1, symbol2, symbol3):
        return self.__request('last_prices/%s/%s/%s/' % (symbol1, symbol2, symbol3), {})

    def convert(self, symbol1, symbol2, amnt):
        params = {'amnt': amnt}
        return self.__request('convert/%s/%s/' % (symbol1, symbol2), params, 'POST')

    def price_stats(self, symbol1, symbol2, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('price_stats/%s/%s/' % (symbol1, symbol2), params, 'POST')

    def ohlcv_hd(self, date, symbol1, symbol2):
        return self.__request('ohlcv/hd/%s/%s/%s/' % (date, symbol1, symbol2), {})

    def order_book(self, symbol1, symbol2, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('order_book/%s/%s/' % (symbol1, symbol2), params)

    def trade_history(self, symbol1, symbol2, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('trade_history/%s/%s/' % (symbol1, symbol2), params)

    # TODO Private API calls:

