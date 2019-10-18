#!/usr/bin/env python

import cc
import json

def d(j):
    print (json.dumps(j, sort_keys=True, indent=4, separators=(',', ': ')))

def main():
    api = cc.BlockStream()
#    d(api.get_tx('txid'))
#    d(api.get_address('address'))
#    d(api.get_scripthash('scripthash'))
#    d(api.get_block('blockhash'))
#    d(api.get_blocks(9))
#    d(api.get_blocks_tip_height())
#    d(api.get_mempool())
#    d(api.get_mempool_txids())
#    d(api.get_mempool_recent())
    d(api.get_fee_estimates())


if __name__ == '__main__':
    main()
