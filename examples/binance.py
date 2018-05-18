#!/usr/bin/env python

import cc
import json

def d(j):
    print (json.dumps(j, sort_keys=True, indent=4, separators=(',', ': ')))

def main():
    public_key = ''
    private_key = ''
    api = cc.Binance()
    d(api.ping())
#    d(api.time())
#    d(api.exchange_info())
#    d(api.depth(symbol='ETHBTC'))
#    d(api.trades(symbol='ETHBTC'))
#    d(api.agg_trades(symbol='ETHBTC'))
#    d(api.klines(symbol='ETHBTC', interval='4h'))
#    d(api.ticker_24hr(symbol='ETHBTC'))
#    d(api.ticker_price(symbol='ETHBTC'))
#    d(api.ticker_book_ticker(symbol='ETHBTC'))
#    api.set_credential(public_key, private_key)
#    d(api.order(symbol='ETHBTC', side='BUY', type='MARKET', quantity=1))
#    d(api.order_test(symbol='ETHBTC', side='BUY', type='MARKET', quantity=1))
#    d(api.order_status(symbol='ETHBTC', orderId=0))
#    d(api.order_cancel(symbol='ETHBTC', orderId=0))
#    d(api.open_orders())
#    d(api.all_orders(symbol='ETHBTC'))
#    d(api.account())
#    d(api.my_trades(symbol='ETHBTC'))

if __name__ == '__main__':
    main()

