import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, prcps = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        prsp = float(row[3])

        prcps.append(prsp)
        dates.append(current_date)

filename1 = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates1, prcps1 = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        prsp = float(row[3])

        prcps1.append(prsp)
        dates1.append(current_date)

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(dates, prcps, c='white')

ax.set_title("PRCP - 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("ежедневные осадки", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)


plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(dates1, prcps1, c='blue')

ax.set_title("PRCP - 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("ежедневные осадки death_valley", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()