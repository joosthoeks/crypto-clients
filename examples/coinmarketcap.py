#!/usr/bin/env python

import cc
import json

def d(j):
    print (json.dumps(j, sort_keys=True, indent=4, separators=(',', ': ')))

def main():
    api = cc.CoinMarketCap()
    d(api.get_listings())
#    d(api.get_ticker(start=0, limit=2, convert='EUR'))
#    d(api.get_ticker_id(2))
#    d(api.get_global())

if __name__ == '__main__':
    main()

