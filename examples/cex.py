#!/usr/bin/env python

import cc
import json

def d(j):
    print (json.dumps(j, sort_keys=True, indent=4, separators=(',', ': ')))

def main():
    user_key = ''
    public_key = ''
    private_key = ''
    api = cc.Cex()
    d(api.currency_limits())
#    d(api.ticker('ETH', 'BTC'))
#    d(api.tickers('ETH', 'BTC'))
#    d(api.last_price('ETH', 'BTC'))
#    d(api.last_prices('ETH', 'BTC', 'EUR'))
#    d(api.convert('ETH', 'BTC', 2.5))
#    d(api.price_stats('ETH', 'BTC', lastHours=24, maxRespArrSize=100))
#    d(api.ohlcv_hd('YYYYMMDD', 'ETH', 'BTC'))
#    d(api.order_book('ETH', 'BTC'))
#    d(api.trade_history('ETH', 'BTC'))
#    api.set_credential(user_id, public_key, private_key)
#    d(api.balance())
#    d(api.open_orders())
#    d(api.active_orders_status([0]))
#    d(api.archived_orders('ETH', 'BTC'))
#    d(api.cancel_order(0))
#    d(api.cancel_orders('ETH', 'BTC'))
#    d(api.place_order('ETH', 'BTC', type='buy', amount=12))
#    d(api.get_order(0))
#    d(api.get_order_tx(0))
#    d(api.get_address('BTC'))
#    d(api.get_myfee())
#    d(api.cancel_replace_order('ETH', 'BTC', 'buy'))
#    d(api.open_position('ETH', 'BTC', symbol='BTC', msymbol='BTC'))
#    d(api.get_position(0))
#    d(api.open_positions('ETH', 'BTC'))
#    d(api.close_position('ETH', 'BTC', 0))
#    d(api.archived_positions('ETH', 'BTC'))
#    d(api.get_marginal_fee('ETH', 'BTC'))

if __name__ == '__main__':
    main()

