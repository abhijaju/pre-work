
import config
import random
from datetime import date, timedelta

dates = []
now = date.today()
onedayless = timedelta(days=1)
for i in range(0, config.NUM_DATES):
  dates.append(now)
  now = now - onedayless


fp = open("type1_data.csv", "w+")

for i in range(0, config.NUM_BACKTESTS):
  for day in dates:
    fp.write( "%s,%d,%f\n" % (str(day), i, random.random()) )

fp.close()
