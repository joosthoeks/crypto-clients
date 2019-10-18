

import requests


class BlockStream(object):

    def __init__(self, url='https://blockstream.info/api/'):
        self.__url = url

    def __request(self, endpoint):
        full_url = '%s%s' % (self.__url, endpoint)
        r = requests.get(full_url)
        return r.json()

    # transactions:
    def get_tx(self, txid):
        return self.__request('tx/%s' % txid)

    # addresses:
    def get_address(self, address):
        return self.__request('address/%s' % address)

    def get_scripthash(self, hash):
        return self.__request('scripthash/%s' % hash)

    # blocks:
    def get_block(self, hash):
        return self.__request('block/%s' % hash)

    def get_blocks(self, start_height):
        return self.__request('blocks/%s' % start_height)

    def get_blocks_tip_height(self):
        return self.__request('blocks/tip/height')

    # mempool:
    def get_mempool(self):
        return self.__request('mempool')

    def get_mempool_txids(self):
        return self.__request('mempool/txids')

    def get_mempool_recent(self):
        return self.__request('mempool/recent')

    # fee estimates:
    def get_fee_estimates(self):
        return self.__request('fee-estimates')
