#learner_id  country   in_course   unit   avg_score    completion   inv_rate
#bar chart- liczba osob zaczela chapter/laczna liczba osob
import sqlite3
import bar_chart as bar
conn = sqlite3.connect('PearsonData')
cur = conn.cursor() 

chapter = []
people = []
with_teachers = []
percentage = []

cur.execute("""SELECT COUNT(*)
                FROM (SELECT
                        DISTINCT learner_id
                        FROM data2018)""")
all_people = int(str(cur.fetchall())[2:-3])

print(all_people)
#Give me distinct country
cur.execute("""SELECT 
               DISTINCT
               unit FROM data2018
               ORDER BY unit""")
distinct_chapter = cur.fetchall()

#Search for number of people from country X
for x in distinct_chapter:
    cur.execute("""SELECT COUNT(*) 
                     FROM  (SELECT 
                            DISTINCT learner_id
                            FROM data2018 
                            WHERE unit=(?))""", (x) )
    how_many = cur.fetchall()
    chapter.append(x[0])
    people.append(how_many[0][0])

a = 0
copy_people = people.copy()

chapter[0] = 'nothing'
for i in range(1,18):
    if i <=12:
        chapter[i] = '{}'.format(i)
    elif i <=16:
        chapter[i] = 'R{}'.format(i-12)
    else:
        chapter[i] = 'VP'
for i in range(2,13):
    if i <=9:
        people[i] = copy_people[i+3]
    elif i<=12:
        people[i] = copy_people[i-8]
        
        
chapter = chapter[1:]
people =people[1:]

for x in range(len(chapter)):
    percentage.append((people[x]/all_people)*100)





        
bar.bar_chart(chapter, percentage, "The ratio of started units","Percentage","int")        

        
        
        
















