#learner_id  country   in_course   unit   avg_score    completion   inv_rate
import sqlite3
import bar_chart as bar

completion = []
temporary = []
dist_units = []

conn = sqlite3.connect('PearsonData')
cur = conn.cursor() 

#Give me distinct units
cur.execute("""SELECT 
               DISTINCT
               unit from data2018     
               ORDER BY unit""")   # WHERE unit != '' is to low
distinct_units = cur.fetchall()
if distinct_units[0] == ('',): 
    distinct_units = distinct_units[1:]
    
temporary.append(distinct_units[0])
temporary.append(distinct_units[4])
temporary.append(distinct_units[5])
temporary.append(distinct_units[6])
temporary.append(distinct_units[7])
temporary.append(distinct_units[8])
temporary.append(distinct_units[9])
temporary.append(distinct_units[10])
temporary.append(distinct_units[11])
temporary.append(distinct_units[1])
temporary.append(distinct_units[2])
temporary.append(distinct_units[3])
temporary.append(distinct_units[12])
temporary.append(distinct_units[13])
temporary.append(distinct_units[14])
temporary.append(distinct_units[15])
temporary.append(distinct_units[16])
distinct_units  = temporary

for x in distinct_units:    
    cur.execute("""SELECT AVG(completion) 
                     FROM  (SELECT 
                            completion
                            FROM data2018 
                            WHERE unit=(?))""", (x) )
    how_many = cur.fetchall()
    completion.append(how_many[0][0]*100)
    
for x in distinct_units:
    dist_units.append(x[0])   
dist_units[12] = 'R3'
dist_units[13] = 'R6'
dist_units[14] = 'R9'
dist_units[15] = 'R12'
dist_units[16] = 'VP'


bar.bar_chart(dist_units, completion, "Unit", "Completion", "int")


