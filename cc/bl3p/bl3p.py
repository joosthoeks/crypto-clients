

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
        post_data = urllib.parse.urlencode(params)
        body = ('%s%c%s' % (endpoint, 0x00, post_data)).encode()
        sec_key_bin = base64.b64decode(self.__sec_key)
        signature_bin = hmac.new(sec_key_bin, body, hashlib.sha512)
        signature = base64.b64encode(signature_bin.digest()).decode()
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

    # TODO Authenticated API | HTTP Calls
    def get_btc_multiplier(self):
        return 100000000

    def get_eur_multiplier(self):
        return 100000

    def add_order(self, market, order_type, order_amount, order_price):
        params = {
            'type' : order_type,
            'amount_int' : order_amount,
            'price_int' : order_price,
            'fee_currency' : 'BTC'
        }
        return self.__request('%s/money/order/add' % market, params)

    def cancel_order(self, market, order_id):
        params = {'order_id': order_id}
        return self.__request('%s/money/order/cancel' % market, params)

    def order_info(self, market, order_id):
        params = {'order_id' : order_id}
        return self.__request('%s/money/order/result' % market, params, True)

    def get_all_active_orders(self, market):
        return self.__request('%s/money/orders' % market, {}, True);

    def full_depth(self, market):
        return self.__request('%s/money/depth/full' % market, {}, True)

    def get_new_deposit_address(self, market):
        return self.__request('%s/money/new_deposit_address' % market, {}, True)

    def get_last_deposit_address(self, market):
        return self.__request('%s/money/deposit_address' % market, {}, True)

    def fetch_last_1000_trades(self, market, trade_id):
        params = {'trade_id': trade_id}
        return self.__request('%s/trades' % market, params)

    def get_balances(self):
        params = {}
        return self.__request('GENMKT/money/info', params, True)
    
    def wallet_history(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('GENMKT/money/wallet/history', params, True)

