

import requests


class Bitnodes(object):

    def __init__(self, url='https://bitnodes.io/api/v1/'):
        self.__url = url

    def __request(self, endpoint, params, method='GET'):
        full_url = '{}{}'.format(self.__url, endpoint)

        if method is 'GET':
            r = requests.get(full_url, params=params)
        if method is 'POST':
            r = requests.post(full_url, data=params)

        return r.json()

    def snapshots(self, timestamp=None, **kwargs):
        params = {}
        params.update(kwargs)
        if timestamp is None:
            return self.__request('snapshots/', params)
        else:
            return self.__request('snapshots/{}/'.format(timestamp), params)

    def nodes(self, address, port, latency=False, method='GET', **kwargs):
        if method is 'GET':
            if latency:
                return self.__request('nodes/{}-{}/latency/'.format(address, port), {})
            else:
                return self.__request('nodes/{}-{}/'.format(address, port), {})
            if method is 'POST':
                params = {}
                params.update(kwargs)
                return self.__request('nodes/{}-{}/'.format(address, port), params, 'POST')

    def leaderboard(self, address=None, port=None, **kwargs):
        params = {}
        params.update(kwargs)
        if address is None and port is None:
            return self.__request('nodes/leaderboard/', params)
        else:
            return self.__request('nodes/leaderboard/{}-{}/'.format(address, port), params)

    def inv_hash(self, inv_hash):
        return self.__request('inv/{}/'.format(inv_hash), {})
