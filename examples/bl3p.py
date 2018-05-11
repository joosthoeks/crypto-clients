#!/usr/bin/env python

import cc
import json

def d(j):
    print (json.dumps(j, sort_keys=True, indent=4, separators=(',', ': ')))

def main():
    public_key = ''
    private_key = ''
    api = cc.Bl3p()
    d(api.ticker('BTCEUR'))
#    d(api.orderbook('BTCEUR'))
#    d(api.trades('BTCEUR'))
#    api.set_credential(public_key, private_key)
#    d(api.order_add('BTCEUR', type='bid', amount_int=100000000, price_int=100000, fee_currency='EUR'))
#    d(api.order_cancel('BTCEUR', 0))
#    d(api.order_result('BTCEUR', 0))
#    d(api.depth_full('BTCEUR'))
#    d(api.wallet_history(currency='BTC'))
#    d(api.new_deposit_address('BTC'))
#    d(api.deposit_address('BTC'))
#    d(api.withdraw(currency='BTC', address='btc_address', amount_int=100000000))
#    d(api.info())
#    d(api.orders('BTCEUR'))
#    d(api.orders_history('BTCEUR'))
#    d(api.trades_fetch('BTCEUR'))

if __name__ == '__main__':
    main()

