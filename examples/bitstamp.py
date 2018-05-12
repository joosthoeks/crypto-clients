#!/usr/bin/env python

import cc
import json

def d(j):
    print (json.dumps(j, sort_keys=True, indent=4, separators=(',', ': ')))

def main():
    customer_id = ''
    public_key = ''
    private_key = ''
    api = cc.Bitstamp()
    d(api.ticker('btceur'))
#    d(api.ticker_hour('btceur'))
#    d(api.order_book('btceur'))
#    d(api.transactions('btceur'))
#    d(api.trading_pairs_info())
#    api.set_credential(customer_id, public_key, private_key)
#    d(api.balance())
#    d(api.user_transactions())
#    d(api.open_orders())
#    d(api.cancel_order(0))
#    d(api.buy('btceur', amount=100000000, price=100000, limit_price=100000))
#    d(api.buy_market('btceur', 100000000))
#    d(api.sell('btceur', amount=100000000, price=100000, limit_price=100000))
#    d(api.sell_market('btceur', 100000000))
#    d(api.withdrawal_requests())
#    d(api.ltc_withdrawal(amount=100000000, address='ltc_address'))
#    d(api.ltc_address())
#    d(api.eth_withdrawal(amount=100000000, address='eth_address'))
#    d(api.eth_address())
#    d(api.bch_withdrawal(amount=100000000, address='bch_address'))
#    d(api.bch_address())
#    d(api.transfer_to_main(amount=100000000, currency='btc'))
#    d(api.transfer_from_main(amount=100000000, currency='btc', subAccount='sub_account'))
#    d(api.xrp_withdrawal(amount=100000000, address='xrp_address'))
#    d(api.xrp_address())
#    d(api.withdrawal_open(amount=100000, account_currency='EUR', name='user_name', IBAN='user_iban', BIC='bank_bic', address='user_address', postal_code='user_postal_code', city='user_city', country='user_country_code', type='sepa'))
#    d(api.withdrawal_status(0))
#    d(api.withdrawal_cancel(0))
#    d(api.liquidation_address_new('EUR'))
#    d(api.liquidation_address_info())

if __name__ == '__main__':
    main()

