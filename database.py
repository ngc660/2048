import sqlite3

bd = sqlite3.connect("2048.sqlite")

cur = bd.cursor()
cur.execute("""
create table if not exists Records(
    name text,
    score integer
) """)

cur.execute("""
SELECT name, max(score) score from Records	 
GROUP by name
ORDER by score DESC
Limit 3
""")

result = cur.fetchall()
print(result)
cur.close()