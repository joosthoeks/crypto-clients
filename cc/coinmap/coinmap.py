

import requests


class CoinMap(object):

    def __init__(self, url='https://coinmap.org/api/v1/'):
        self.__url = url

    def __request(self, endpoint, params, method='GET', credential=False):
        full_url = '%s%s' % (self.__url, endpoint)
        if credential:
            '''
            TODO
            '''
        else:
            r = requests.get(full_url, params=params)
#        response_code = r.status_code
#        if response_code != 200:
#            raise Exception('Exception response code: %d' % response_code)
        return r.json()

    def venues(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('venues', params)
    
    def new_venue(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('venues', params, 'POST', True)

    def read_venue(self, id):
        return self.__request('venues/%s' % id, {})

    def update_venue(self, id, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('venues/%s' % id, params, 'PUT', True)

    def delete_venue(self, id):
        return self.__request('venues/%s' % id, {}, 'DELETE', True)

    def comments(self, id):
        return self.__request('venues/%s/comments' % id, {})

    def create_comment(self, id, text):
        params = {'text': text}
        return self.__request('venues/%s/comments' % id, params, 'POST', True)

    def ratings(self, id):
        return self.__request('venues/%s/ratings' % id, {})

    def create_rating(self, id, vote):
        params = {'vote': vote}
        return self.__request('venues/%s/ratings' % id, params, 'POST', True)

