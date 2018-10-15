from coinbase.wallet.client import Client
from Configuration import *
import time

client = Client("", "")
euro_wallet = "EUR Wallet"
btc_wallet = "BTC Wallet"
bank_account_payment_method = 0
credit_card_payment_method = 1
eur_wallet_payment_method = 2


def get_rates():
    rates = client.get_exchange_rates(currency='BTC')
    rates['time'] = time.time()
    return rates


def get_rate_usd():
    rates = get_rates()
    return rates.rates.USD


def get_rate_eur():
    rates = get_rates()
    return rates.rates.EUR


def print_info_accounts():
    accounts = client.get_accounts()
    for account in accounts.data:
        balance = account.balance
        print("%s: %s %s" % (account.name, balance.amount, balance.currency))


def get_account_balance(name):
    amount = -1
    accounts = client.get_accounts()
    for account in accounts.data:
        if account.name == name:
            balance = account.balance
            amount = balance.amount
    return amount


def buy_bitcoin(amount, payment_method_id):
    account = client.get_primary_account()
    buy = account.buy(amount=amount,
                      currency="BTC",
                      payment_method=payment_method_id)
    return buy


def sell_bitcoin(amount, payment_method_id):
    account = client.get_primary_account()
    sell = account.sell(amount=amount,
                        currency="BTC",
                        payment_method=payment_method_id)
    return sell


def get_payment_method_id():
    # PTO Bank 0, Credit Card 1
    method_id = "-1"
    if CURRENT_STAGE == DEVELOPMENT_STAGE:
        payment_method = client.get_payment_methods()[credit_card_payment_method]
        method_id = payment_method.id
    elif CURRENT_STAGE == PRODUCTION_STAGE:
        payment_method = client.get_payment_methods()[euro_wallet]
        print(payment_method)
        method_id = payment_method.id
    return method_id


def get_buy_price(currency_pair):
    return client.get_buy_price(currency_pair=currency_pair)


def get_sell_price(currency_pair):
    return client.get_sell_price(currency_pair=currency_pair)
