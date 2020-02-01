import pandas as pd
import sqlite3

##import the csv
df = pd.read_csv(r'C:\Users\lauw02\Desktop\stats 418\Stats-418-W20\hw1\q5\data.csv')
##convert it to a SQL databse

##print(df.head())
conn = sqlite3.connect('db2.sqlite3')
c = conn.cursor()
##create table
c.execute('CREATE TABLE DATA (Date date, S1 int, S2 int, S3 int, S4 int, S5 int,'
          ' S6 int, S7 int, S8 int, S9 int, S10 int)')
conn.commit()

df.to_sql('DATA', conn, if_exists='replace', index = False)
c.execute('''  
SELECT * FROM DATA
          ''')

for row in c.fetchall():
    print (row)

#c.execute('DROP TABLE DATA')