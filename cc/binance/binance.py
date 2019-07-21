

import requests
import hashlib
import hmac
import urllib.parse
import time


class Binance(object):

    def __init__(self, url='https://api.binance.com/api/'):
        self.__url = url

    def set_credential(self, pub_key, sec_key):
        self.__pub_key = pub_key
        self.__sec_key = sec_key

    def __get_credential(self, params):
        params.update({'timestamp': (int(time.time()) * 1000000)})
        query_str = urllib.parse.urlencode(params)
        signature = hmac.new(
                self.__sec_key.encode('utf8'),
                msg=query_str.encode('utf8'),
                digestmod=hashlib.sha256
                ).hexdigest()
        headers = {
                'X-MBX-APIKEY': self.__pub_key
                }
        return signature, headers

    def __request(self, endpoint, params, method='GET', credential=False):
        full_url = '%s%s' % (self.__url, endpoint)
        if credential:
            signature, headers = self.__get_credential(params)
            params.update({'signature': signature})
            if method is 'POST':
                r = requests.post(full_url, data=params, headers=headers)
            elif method is 'DELETE':
                r = requests.delete(full_url, data=params, headers=headers)
            else:
                r = requests.get(full_url, params=params, headers=headers)
        else:
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

    # Account endpoints:
    def order(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('v3/order', params, 'POST', True)

    def order_test(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('v3/order/test', params, 'POST', True)

    def order_status(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('v3/order', params, 'GET', True)

    def order_cancel(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('v3/order', params, 'DELETE', True)

    def open_orders(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('v3/openOrders', params, 'GET', True)

    def all_orders(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('v3/allOrders', params, 'GET', True)

    def account(self):
        return self.__request('v3/account', {}, 'GET', True)

    def my_trades(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('v3/myTrades', params, 'GET', True)


