#!/usr/bin/env python

import cc
import json

def d(j):
    print (json.dumps(j, sort_keys=True, indent=4, separators=(',', ': ')))

def main():
    api = cc.CoinMap()
    d(api.venues(query='Pizza'))
#    d(api.new_venue())
#    d(api.read_venue(1))
#    d(api.update_venue())
#    d(api.delete_venue())
#    d(api.comments(1))
#    d(api.create_comment())
#    d(api.ratings(1))
#    d(api.create_rating())

if __name__ == '__main__':
    main()

