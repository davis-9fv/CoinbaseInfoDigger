from Configuration import *
from CoinbaseAPI import *
from Util import *

top_price = (BOTTOM_PRICE * PROFIT) + BOTTOM_PRICE


def get_top_price():
    return top_price


def buy(amount):
    sucesss = False
    balance = get_account_balance(euro_wallet)
    if float(balance) >= amount:
        print("buy")
        btc_price = get_buy_price(CURRENCY_PAIR)
        print("BTC Price %s %s " % (btc_price, CURRENCY_PAIR))
        amount_btc = from_money_to_btc(amount, btc_price)
        print(amount_btc)
        buy = buy_bitcoin(amount_btc, get_payment_method_id())
        print(buy)
        sucesss = True
    else:
        print("Not enough money")
    return sucesss


def sell():
    sucesss = False
    balance = get_account_balance(btc_wallet)
    if float(balance) > 0.000001:
        print("sell")
        btc_price = get_sell_price(CURRENCY_PAIR)
        print("BTC Price %s %s " % (btc_price, CURRENCY_PAIR))
        amount_euro = from_btc_to_money(balance, btc_price)
        print("Amount EURO %s" % amount_euro)
        sell = sell_bitcoin(balance, get_payment_method_id())
        print(sell)
        sucesss = True
    else:
        print("Not enough bitcoins")
    return sucesss
