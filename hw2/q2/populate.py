#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import sqlite3


# In[6]:


df = pd.read_csv(r'C:\Users\lauw02\Desktop\stats 418\Stats-418-W20\hw2\q2\movies.csv')
df.head(1)
recordList = df.get_values()

conn = sqlite3.connect(r'C:\Users\lauw02\Desktop\stats 418\Stats-418-W20\hw2\q1\movieratings.db')


# In[11]:


cursor = conn.cursor()

sqlite_insert_query = """INSERT INTO Movies
                  (title, year,genre, rating, numvotes, plot)
                  VALUES (?, ?, ?, ?, ?, ?);"""
recordList = df.get_values()
cursor.executemany(sqlite_insert_query, recordList)
conn.commit()

