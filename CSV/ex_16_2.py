import csv
from matplotlib import pyplot as plt
from datetime import datetime


filename1 = 'data/sitka_weather_2018_simple.csv'
filename2 = 'data/death_valley_2018_simple.csv'

def get_data(filename, index_hight: int, index_low: int):
    """возвращает данные для построения графика(дата,min temp, max temp)
     в виде словаря"""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            try:
                high = int(row[index_hight])
                low = int(row[index_low])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

        return {"dates": dates, "highs": highs, "lows": lows}

def set_plot(filename_data):
    ax.plot(filename_data["dates"], filename_data["highs"], c='red')
    ax.plot(filename_data["dates"], filename_data["lows"], c='blue')
    plt.fill_between(filename_data["dates"], filename_data["highs"], filename_data["lows"], facecolor='blue', alpha=0.2)

# Нанесение данных на диаграмму.
plt.style.use('seaborn')
fig, ax = plt.subplots()

# Форматирование диаграммы.
title = "Daily high and low temperatures"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)

fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)


set_plot(get_data(filename1, 5, 6))
set_plot(get_data(filename2, 4, 5))

plt.show()