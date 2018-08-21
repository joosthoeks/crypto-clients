#!/usr/bin/env python

import cc
import json

def d(j):
    print (json.dumps(j, sort_keys=True, indent=4, separators=(',', ': ')))

def main():
    key = ''
    api = cc.Bitwise()
    api.set_credential(key)
    d(api.indexes())
#    d(api.indexes_ticker('BITWISE10'))
#    d(api.indexes_history('BITWISE10', exclude_backtests=True))

if __name__ == '__main__':
    main()

