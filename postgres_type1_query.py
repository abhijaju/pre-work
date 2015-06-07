
import config
import psycopg2
import time

conn = psycopg2.connect(database="pre", user="pre", password="pre", host="127.0.0.1", port="5432")
cur = conn.cursor()

SELECT = "SELECT * FROM type1 WHERE strat_id=%s AND date_exp >= '%s' AND date_exp <= '%s'"

fp = open("data/type1_query.csv", "r", 1)
fp_time = open("data/postgres_type1_lookup_query_time.csv", "w+")

for i in range(0, config.NUM_QUERIES):
  print "Query Number: %d" % i
  row = fp.readline().rstrip('\n').split(',')
  lookup_query = SELECT % (row[0], row[1], row[2])

  start = time.time()
  cur.execute(lookup_query)
  time_taken = time.time() - start
  print "Rows returned %d" % cur.rowcount
  fp_time.write("%f\n" % time_taken)

fp.close()
fp_time.close()
conn.close()
