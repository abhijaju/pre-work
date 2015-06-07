
import config
import redis
import time
from datetime import datetime

rdb = redis.StrictRedis('localhost')
fp = open("data/type1_query.csv", "r", 1)
fp_time = open("data/redis_type1_lookup_query_time.csv", "w+")

for i in range(0, config.NUM_QUERIES):
  print "Query Number: %d" % i
  row = fp.readline().rstrip('\n').split(',')
  key = "stratID:"+row[0]
  start_date = row[1].replace("-", "")
  end_date = row[2].replace("-", "")

  start = time.time()
  rdb.zrangebyscore(key, start_date, end_date, withscores=True)
  time_taken = time.time() - start
  fp_time.write("%f\n" % time_taken)

fp.close()
fp_time.close()
