from Core import *
import logging.config
import time
import pandas as pd

logging.config.fileConfig('logging.conf')

if CURRENT_STAGE == PRODUCTION_STAGE:
    logger = logging.getLogger('proLog')
elif CURRENT_STAGE == DEVELOPMENT_STAGE:
    logger = logging.getLogger('root')

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

logging.warning("CURRENT STAGE: %s" % CURRENT_STAGE)
logging.warning("Porcentage margin: %s " % (PROFIT * 100))
logging.info("Bottom price: %s %s" % (BOTTOM_PRICE, CURRENCY))
logging.warning("Top price: %s %s" % (top_price, CURRENCY))

print(get_rate_usd())
# print(get_account_balance(euro_wallet))
# print(buy(2))
# print(sell())
# print(get_payment_method_id())

write_file = True
# path = '/root/'
path = 'C:/tmp/bitcoin/'
output_file = 'bitcoin_usd_by_minute.csv'

rows = []
columns = ['rate_eur','sell_price','buy_price']
dfx = pd.DataFrame(columns=columns)
dfx.to_csv(path + output_file, mode='a', header=True)

while True:
    print(" ")
    rate_eur = get_rate_eur()
    sell_price = get_sell_price(CURRENCY_PAIR).amount
    buy_price = get_buy_price(CURRENCY_PAIR).amount
    logging.debug("Precio Bitcoin %s EUR" % rate_eur)
    logging.debug("Selling price %s EUR" % sell_price)
    logging.debug("Buying price %s EUR" % buy_price)
    time.sleep(1)  # Measured in seconds.

    dfx['rate_eur'] = [rate_eur]
    dfx['sell_price'] = [sell_price]
    dfx['buy_price'] = [buy_price]
    dfx.to_csv(path + output_file, mode='a', header=False)
