import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

# http://pythonforengineers.com/introduction-to-pandas/

data = pd.read_csv("C:/tmp/coindesk-bpi-USD-close_data-2018-02-20_2018-03-20.csv")
# print(data.head())
# data.plot()
# plt.show()

# data = np.genfromtxt("C:/tmp/coindesk-bpi-USD-close_data-2018-02-20_2018-03-20.csv", delimiter=',')

print(data.loc[:,"Close Price"].mean())
print(data.loc[:,"Close Price"].median())



