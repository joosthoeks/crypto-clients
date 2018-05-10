#!/usr/bin/env python

import cc
import json

def d(j):
    print (json.dumps(j, sort_keys=True, indent=4, separators=(',', ': ')))

def main():
    api = cc.Bitstamp()

if __name__ == '__main__':
    main()

