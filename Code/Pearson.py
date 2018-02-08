#learner_id  country   in_course   unit   avg_score    completion   inv_rate
import sqlite3

conn = sqlite3.connect('PearsonData')
cur = conn.cursor()


#Give me distinct ID
cur.execute("""SELECT 
               DISTINCT
               learner_id from data2018""")
distinct_id = cur.fetchall()

#Give me distinct units
cur.execute("""SELECT 
               DISTINCT
               unit from data2018     
               ORDER BY unit""")   # WHERE unit != '' is to low
distinct_units = cur.fetchall()
for x in distinct_units:
    print(x)

#I will repair this                                                            ADD completion > 30%
for x in distinct_id:
    cur.execute("""SELECT COUNT(*) 
                     FROM  (SELECT DISTINCT * 
                            FROM data2018 
                            WHERE learner_id=(?))""", (x) )
thr = cur.fetchall()
print(thr[0][0])
