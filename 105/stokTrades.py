#https://finance.yahoo.com/quote/
import matplotlib.pyplot as plt
import csv
from datetime import datetime

dates = []
values = []

with open('ETH-BTC.csv', newline='') as f:
      reader = csv.reader(f)
      next(reader)
      lastRaw = next(reader)
      for raw in reader:
            dates.append(datetime.strptime(raw[0], "%Y-%m-%d"))
            #values.append(raw[-2])
            values.append((float(raw[-2])-float(lastRaw[-2]))/float(lastRaw[-2]))
            lastRaw = raw
      
plt.plot(dates, values)
plt.plot(dates[-100:], values[-100:])
plt.show()


