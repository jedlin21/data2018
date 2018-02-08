#learner_id  country   in_course   unit   avg_score    completion   inv_rate
#wynik od teachera
import sqlite3
import bar_chart as bar
conn = sqlite3.connect('PearsonData')
cur = conn.cursor() 

cur.execute("""SELECT AVG(avg_score)
                    FROM (SELECT avg_score FROM data2018 WHERE in_course='f')""")
wynik_f = cur.fetchall()[0][0]*100

cur.execute("""SELECT AVG(avg_score)
                    FROM (SELECT avg_score FROM data2018 WHERE in_course='t')""")
wynik_t = cur.fetchall()[0][0]*100



bar.bar_chart(('teacher', 'no teacher'),[wynik_t,wynik_f],"Average score depending on teacher presence", "","float")
