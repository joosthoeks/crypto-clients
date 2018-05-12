

import requests
import time
import hmac
import hashlib


class Cex(object):
    
    def __init__(self, url='https://cex.io/api/'):
        self.__url = url

    def set_credential(self, user_id, pub_key, sec_key):
        self.__user_id = user_id
        self.__pub_key = pub_key
        self.__sec_key = sec_key
    
    def __get_credential(self):
        nonce = int(time.time())
        message = str(nonce) + self.__user_id + self.__pub_key
        signature = hmac.new(
                self.__sec_key.encode('utf8'),
                msg=message.encode('utf8'),
                digestmod=hashlib.sha256
                ).hexdigest().upper()
        return nonce, signature

    def __request(self, endpoint, params, method='GET', credential=False):
        full_url = '%s%s' % (self.__url, endpoint)
        if credential:
            nonce, signature = self.__get_credential()
            credential = {
                    'key': self.__pub_key,
                    'nonce': nonce,
                    'signature': signature,
                    }
            params.update(credential)
            if method is 'POST':
                r = requests.post(full_url, data=params)
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
    def balance(self):
        return self.__request('balance/', {}, 'POST', True)

    def open_orders(self, symbol1=None, symbol2=None):
        if symbol1 is None and symbol2 is None:
            return self.__request('open_orders/', {}, 'POST', True)
        else:
            return self.__request('open_orders/%s/%s/' % (symbol1, symbol2), {}, 'POST', True)

    def active_orders_status(self, orders_list):
        params = {'orders_list': orders_list}
        return self.__request('active_orders_status/', params, 'POST', True)

    def archived_orders(self, symbol1, symbol2, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('archived_orders/%s/%s/' % (symbol1, symbol2), params, 'POST', True)

    def cancel_order(self, id):
        params = {'id': id}
        return self.__request('cancel_order/', params, 'POST', True)

    def cancel_orders(self, symbol1, symbol2):
        return self.__request('cancel_orders/%s/%s/' % (symbol1, symbol2), {}, 'POST', True)

    def place_order(self, symbol1, symbol2, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('place_order/%s/%s/' % (symbol1, symbol2), params, 'POST', True)

    def get_order(self, id):
        params = {'id': id}
        return self.__request('get_order/', params, 'POST', True)

    def get_order_tx(self, id):
        params = {'id': id}
        return self.__request('get_order_tx/', params, 'POST', True)


