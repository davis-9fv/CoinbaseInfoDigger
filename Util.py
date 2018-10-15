def from_money_to_btc(amount, btc_price):
    return amount / float(btc_price)


def from_btc_to_money(amount_btc, btc_price):
    return float(amount_btc) * float(btc_price)
