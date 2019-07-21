

import time
import base64
import hashlib
import hmac
import requests
import urllib.parse


class Bl3p(object):
    
    def __init__(self, url='https://api.bl3p.eu/1/'):
        self.__url = url

    def set_credential(self, pub_key, sec_key):
        self.__pub_key = pub_key
        self.__sec_key = sec_key
    
    def __get_credential(self, endpoint, params):
        params.update({'nonce': str(int(time.time() * 1000000))})
        query_str = urllib.parse.urlencode(params)
        body = ('%s%c%s' % (endpoint, 0x00, query_str))
        sec_key_bin = base64.b64decode(self.__sec_key)
        signature_bin = hmac.new(
                sec_key_bin,
                msg=body.encode('utf8'),
                digestmod=hashlib.sha512
                )
        signature = base64.b64encode(signature_bin.digest()).decode('utf8')
        headers = {
                'Rest-Key': self.__pub_key,
                'Rest-Sign': signature
                }
        return headers

    def __request(self, endpoint, params, credential=False):
        full_url = '%s%s' % (self.__url, endpoint)
        if credential:
            headers = self.__get_credential(endpoint, params)
            r = requests.post(full_url, data=params, headers=headers)
        else:
            r = requests.get(full_url, params=params)
        response_code = r.status_code
        if response_code != 200:
            raise Exception('Exception response code: %d' % response_code)
        return r.json()

    # Public API | HTTP Calls
    def ticker(self, market):
        return self.__request('%s/ticker' % market, {})

    def orderbook(self, market):
        return self.__request('%s/orderbook' % market, {})

    def trades(self, market):
        return self.__request('%s/trades' % market, {})

    # Authenticated API | HTTP Calls
    def order_add(self, market, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('%s/money/order/add' % market, params, True)

    def order_cancel(self, market, order_id):
        params = {'order_id': order_id}
        return self.__request('%s/money/order/cancel' % market, params, True)

    def order_result(self, market, order_id):
        params = {'order_id': order_id}
        return self.__request('%s/money/order/result' % market, params, True)

    def depth_full(self, market):
        return self.__request('%s/money/depth/full' % market, {}, True)

    def wallet_history(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('GENMKT/money/wallet/history', params, True)

    def new_deposit_address(self, currency):
        params = {'currency': currency}
        return self.__request('GENMKT/money/new_deposit_address', params, True)

    def deposit_address(self, currency):
        params = {'currency': currency}
        return self.__request('GENMKT/money/deposit_address', params, True)

    def withdraw(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('GENMKT/money/withdraw', params, True)

    def info(self):
        return self.__request('GENMKT/money/info', {}, True)

    def orders(self, market):
        return self.__request('%s/money/orders' % market, {}, True)

    def orders_history(self, market, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('%s/money/orders/history' % market, params, True)

    def trades_fetch(self, market, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('%s/money/trades/fetch' % market, params, True)

