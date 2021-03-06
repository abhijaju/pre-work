
import config
import psycopg2
import time

conn = psycopg2.connect(database="pre", user="pre", password="pre", host="127.0.0.1", port="5432")
cur = conn.cursor()

cur.execute("DELETE from type1_without_index")
conn.commit

INSERT = "INSERT INTO type1_without_index (date_exp, strat_id, ret) VALUES %s"
TUPLE = "('%s', %s, %s)"

fp = open("data/type1_data.csv", "r", 1)
fp_time = open("data/postgres_type1_insert_query_time_without_index.csv", "w+")

for i in range(0, config.NUM_BACKTESTS):
  all_tuples = ""
  print "Backtest Number: %d" % i
  for day in range(0, config.NUM_DATES):
    row = fp.readline().rstrip('\n').split(',')
    all_tuples += TUPLE % (row[0], row[1], row[2])
    if day != config.NUM_DATES - 1:
      all_tuples += ", "

  insert_query = INSERT % all_tuples
  start = time.time()
  cur.execute(insert_query)
  conn.commit()
  time_taken = time.time() - start
  fp_time.write("%f\n" % time_taken)


fp.close()
fp_time.close()
conn.close()
