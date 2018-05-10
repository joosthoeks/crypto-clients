#!/usr/bin/env python

import cc
import json

def d(j):
    print (json.dumps(j, sort_keys=True, indent=4, separators=(',', ': ')))

def main():
    api = cc.CoinCap()
    d(api.get_coins())
#    d(api.get_map())
#    d(api.get_front())
#    d(api.get_global())
#    d(api.get_page('BTC'))
#    d(api.get_history('BTC'))
#    d(api.get_history_1day('BTC'))
#    d(api.get_history_7day('BTC'))
#    d(api.get_history_30day('BTC'))
#    d(api.get_history_90day('BTC'))
#    d(api.get_history_180day('BTC'))
#    d(api.get_history_365day('BTC'))

if __name__ == '__main__':
    main()

