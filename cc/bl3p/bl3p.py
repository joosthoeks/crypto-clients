

import base64
import hashlib
import hmac
import json
import requests
import urllib.parse


class Bl3p(object):
    
    def __init__(self, url, pub_key, sec_key):
        self.url = url
        self.pub_key = pub_key
        self.sec_key = sec_key
    
    def __request(self, path, params):
        post_data = urllib.parse.urlencode(params)

        body = ('%s%c%s' % (path, 0x00, post_data)).encode()

        sec_key_bin = base64.b64decode(self.sec_key)

        signature_bin = hmac.new(sec_key_bin, body, hashlib.sha512)

        signature = base64.b64encode(signature_bin.digest()).decode()

        fullpath = '%s%s' % (self.url, path)

        headers = {
                'Rest-Key': self.pub_key,
                'Rest-Sign': signature
                }

        r = requests.get(fullpath, headers=headers, data=post_data)

        response_code = r.status_code
        if response_code != 200:
            raise Exception('unexpected response code: %d' % response_code)

        return r.json()

    def __t(self, market):
        return market.replace('/', '')

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
        market = self.__t(market)
        return self.__request('%s/money/order/add' % market, params)

    def cancel_order(self, market, order_id):
        params = { 'order_id' : order_id }
        market = self.__t(market)
        return self.__request('%s/money/order/cancel' % market, params)

    def order_info(self, market, order_id):
        params = { 'order_id' : order_id }
        market = self.__t(market)
        return self.__request('%s/money/order/result' % market, params)

    def get_all_active_orders(self, market):
        market = self.__t(market)
        return self.__request('%s/money/orders' % market, { });

    def full_depth(self, market):
        market = self.__t(market)
        return self.__request('%s/money/depth/full' % market, { })

    def get_new_deposit_address(self, market):
        market = self.__t(market)
        return self.__request('%s/money/new_deposit_address' % market, { })

    def get_last_deposit_address(self, market):
        market = self.__t(market)
        return self.__request('%s/money/deposit_address' % market, { })

    def fetch_last_1000_trades(self, market, trade_id):
        params = { 'trade_id' : trade_id }
        market = self.__t(market)
        return self.__request('%s/money/trades/fetch' % market, params)

    def get_balances(self):
        params = { }
        return self.__request('GENMKT/money/info', params)
    
    def wallet_history(self, currency, n):
        params = { 'currency' : currency, 'recs_per_page' : n }
        return self.__request('GENMKT/money/wallet/history', params)

