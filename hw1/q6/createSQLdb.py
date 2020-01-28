import pandas as pd
import sqlite3

##import the csv
df = pd.read_csv(r'C:\Users\lauw02\Desktop\stats 418\Stats-418-W20\hw1\q5\data.csv')
##convert it to a SQL databse

##print(df.head())
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
##create table
c.execute('CREATE TABLE DATA (Date date, S1 text, S2 text, S3 text, S4 text, S5 text,'
          ' S6 text, S7 text, S8 text, S9 text, S10 text)')
conn.commit()

df.to_sql('DATA', conn, if_exists='replace', index = False)
c.execute('''  
SELECT * FROM DATA
          ''')

for row in c.fetchall():
    print (row)

#c.execute('DROP TABLE DATA')