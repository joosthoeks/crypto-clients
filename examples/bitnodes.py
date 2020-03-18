

import cc
from pprint import pprint as pp


def main():
    api = cc.Bitnodes()
    pp(api.snapshots(limit=10, page=2))
#    pp(api.snapshots('latest', field='coordinates'))
#    pp(api.snapshots('latest', field='user_agents'))
#    pp(api.nodes('IP_NUMBER', '8333'))
#    pp(api.nodes('IP_NUMBER', '8333', True))
#    pp(api.nodes('IP_NUMBER', '8333', False, 'POST', bitcoin_address=''))
#    pp(api.leaderboard(limit=10, page=2))
#    pp(api.leaderboard('IP_NUMBER', '8333'))
#    pp(api.inv_hash('INV_HASH'))


if __name__ == '__main__':
    main()
