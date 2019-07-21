

import requests
import time
import hmac
import hashlib


class Bitstamp(object):

    def __init__(self, url='https://www.bitstamp.net/api/v2/'):
        self.__url = url
    
    def set_credential(self, customer_id, pub_key, sec_key):
        self.__customer_id = customer_id
        self.__pub_key = pub_key
        self.__sec_key = sec_key
    
    def __get_credential(self):
        nonce = int(time.time() * 1000000)
        message = str(nonce) + str(self.__customer_id) + self.__pub_key
        signature = hmac.new(
                self.__sec_key.encode('utf8'),
                msg=message.encode('utf8'),
                digestmod=hashlib.sha256
                ).hexdigest().upper()
        return nonce, signature

    def __request(self, endpoint, params, credential=False):
        full_url = '%s%s' % (self.__url, endpoint)
        if credential:
            nonce, signature = self.__get_credential()
            credential = {
                    'key': self.__pub_key,
                    'nonce': nonce,
                    'signature': signature,
                    }
            params.update(credential)
            r = requests.post(full_url, data=params)
        else:
            r = requests.get(full_url, params=params)
        response_code = r.status_code
        if response_code != 200:
            raise Exception('Exception response code: %d' % response_code)
        return r.json()

    # Public data functions:
    def ticker(self, market):
        return self.__request('ticker/%s/' % market, {})

    def ticker_hour(self, market):
        return self.__request('ticker_hour/%s/' % market, {})
    
    def order_book(self, market):
        return self.__request('order_book/%s/' % market, {})

    def transactions(self, market, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('transactions/%s/' % market, params)

    def trading_pairs_info(self):
        return self.__request('trading-pairs-info/', {})

    # Private functions:
    def balance(self, market=None):
        if market is None:
            return self.__request('balance/', {}, True)
        else:
            return self.__request('balance/%s/' % market, {}, True)

    def user_transactions(self, market=None, **kwargs):
        params = {}
        params.update(kwargs)
        if market is None:
            return self.__request('user_transactions/', params, True)
        else:
            return self.__request('user_transactions/%s/' % market, params, True)

    def open_orders(self, market=None):
        if market is None:
            return self.__request('open_orders/all/', {}, True)
        else:
            return self.__request('open_orders/%s/' % market, {}, True)

    def cancel_order(self, id):
        params = {'id': id}
        return self.__request('cancel_order/', params, True)

    def buy(self, market, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('buy/%s/' % market, params, True)

    def buy_market(self, market, amount):
        params = {'amount': amount}
        return self.__request('buy/market/%s/' % market, params, True)

    def sell(self, market, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('sell/%s/' % market, params, True)

    def sell_market(self, market, amount):
        params = {'amount': amount}
        return self.__request('sell/market/%s/' % market, params, True)

    def withdrawal_requests(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('withdrawal-requests/', params, True)

    def ltc_withdrawal(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('ltc_withdrawal/', params, True)

    def ltc_address(self):
        return self.__request('ltc_address/', {}, True)

    def eth_withdrawal(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('eth_withdrawal/', params, True)

    def eth_address(self):
        return self.__request('eth_address/', {}, True)

    def bch_withdrawal(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('bch_withdrawal/', params, True)

    def bch_address(self):
        return self.__request('bch_address/', {}, True)

    def transfer_to_main(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('transfer-to-main/', params, True)

    def transfer_from_main(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('transfer-from-main/', params, True)

    def xrp_withdrawal(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('xrp_withdrawal/', params, True)

    def xrp_address(self):
        return self.__request('xrp_address/', {}, True)

    def withdrawal_open(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('withdrawal/open/', params, True)

    def withdrawal_status(self, id):
        params = {'id': id}
        return self.__request('withdrawal/status/', params, True)

    def withdrawal_cancel(self, id):
        params = {'id': id}
        return self.__request('withdrawal/cancel/', params, True)

    def liquidation_address_new(self, liquidation_currency):
        params = {'liquidation_currency': liquidation_currency}
        return self.__request('liquidation_address/new/', params, True)

    def liquidation_address_info(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('liquidation_address/info/', params, True)

