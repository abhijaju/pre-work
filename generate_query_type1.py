
import config
import random
from datetime import date, timedelta
import math

fp = open("data/type1_query.csv", "w+")

now = date.today()
for i in range(0, config.NUM_QUERIES):
  strat_id = math.floor(random.random()*1000)
  end_date = now - timedelta(days=math.floor(random.random()*1000))
  start_date = end_date - timedelta(days=math.floor(random.random()*1000))
  fp.write("%d,%s,%s\n" %  ( strat_id, str(start_date), str(end_date)))

fp.close()
