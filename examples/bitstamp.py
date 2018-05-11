#!/usr/bin/env python

import cc
import json

def d(j):
    print (json.dumps(j, sort_keys=True, indent=4, separators=(',', ': ')))

def main():
    customer_id = ''
    public_key = ''
    private_key = ''
    api = cc.Bitstamp()
    d(api.ticker('btceur'))
    d(api.ticker_hour('btceur'))
    d(api.order_book('btceur'))
    d(api.transactions('btceur'))
    d(api.trading_pairs_info())
    api.set_credential(customer_id, public_key, private_key)
    d(api.balance())
    d(api.user_transactions())
    d(api.open_orders())
    d(api.cancel_order(0))


if __name__ == '__main__':
    main()

