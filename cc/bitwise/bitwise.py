

import requests


class Bitwise(object):

    def __init__(self, url='https://api.bitwiseinvestments.com/api/v1/'):
        self.__url = url

    def set_credential(self, key):
        self.__key = key

    def __get_credential(self):
        headers = {
                'Authorization': self.__key,
                'Accept': 'application/json'
                }
        return headers

    def __request(self, endpoint, params):
        full_url = '%s%s' % (self.__url, endpoint)
        headers = self.__get_credential()
        r = requests.get(full_url, params=params, headers=headers)
        response_code = r.status_code
        if response_code != 200:
            raise Exception('Exception response code: %d' % response_code)
        return r.json()

    def indexes(self):
        return self.__request('indexes', {})

    def indexes_ticker(self, name):
        return self.__request('indexes/%s/ticker' % name, {})

    def indexes_history(self, name, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('indexes/%s/history' % name, params)

