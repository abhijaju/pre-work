
import config
import redis
import time
from datetime import datetime

rdb = redis.StrictRedis('localhost')
fp = open("data/type1_data.csv", "r", 1)
fp_time = open("data/redis_type1_insert_query_time.csv", "w+")

for i in range(0, config.NUM_BACKTESTS):
  print "Backtest Number: %d" % i
  all_tuples = ()
  rdb.delete("stratID:"+str(i))
  for day in range(0, config.NUM_DATES):
    row = fp.readline().rstrip('\n').split(',')
    date = row[0].replace("-", "")
    all_tuples += (int(date), row[2])

  # to separate out the conversions
  start = time.clock()
  rdb.zadd("stratID:"+str(i), *all_tuples)
  time_taken = time.clock() - start
  fp_time.write("%f\n" % time_taken)

fp.close()
fp_time.close()
