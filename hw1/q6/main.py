#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import sqlite3
import datetime as dt


# In[3]:


# Use the same dataset as segment 5 for this question. Connect to your sqlite3 database with
data = sqlite3.connect('db.sqlite3')
# Python and export your data into a pandas DataFrame.
df = pd.read_sql_query("SELECT * FROM sales", data)

df.sale_date = pd.to_datetime(df.sale_date)
df.store_name = df.store_name.astype(str)


# In[4]:


df.info()
df.head()


# In[78]:


# Write a pandas program ( hw1/q6/main.py ) that outputs the answers to the following queries,
# one per line:
# 6.1 Which store had the highest mean sale in 2017?
## take the average of all sales per day for each store

##df.groupby(df.store_name).mean().sort_values(by='num_sold', ascending=False)
##pd.strftime("%Y", df.sale_date)
##df.sale_date.dt.strftime("%Y")
df_17 = df[(df.sale_date>='2017') & (df.sale_date<'2018')]
df_17.groupby(df_17.store_name).mean().sort_values(by='num_sold', ascending=False)


# In[41]:


# 6.2 Which day showed the highest variance in sales across different stores?
##calculate variance in S1 thru S10 for a single day
df[df.sale_date == '2017-01-01'].var()

start_date = df.sale_date.sort_values()[0].date()
end_date = df.sale_date.sort_values().iloc[-1].date()
daterange = pd.date_range(start_date, end_date)
df_new = pd.DataFrame(columns=[])
variances = list()

for single_date in daterange:
    ##df_new.append(pd.Series(df[df.sale_date == single_date].num_sold.var()),ignore_index=True)
    ##print(df[df.sale_date == single_date].num_sold.var())
    #variances.append( df[df.sale_date == single_date].num_sold.var() )
    ##you'll have to make a df with the sale date AND the variance for that sale date
    variances.append( ( single_date, df[df.sale_date == single_date].num_sold.var()) )
    ##df_new.append(pd.Series(df[df.sale_date == single_date].num_sold.var()),ignore_index=True)
#max(variances)
max(variances, key=lambda item:item[1])

## 2017-03-16 had the highest variance in sales across all stores


# In[39]:


# 6.3 Which year showed the highest median sale for the store S5?
# df[df.store_name == 'S5']
# start_year = dt.datetime(2017,1,1)
# end_year = dt.datetime(2020,1,1)

# yearrange = pd.date_range(start_year,end_year, freq = 'Y')
# #yearrange
# for single_year in yearrange:
#     print(df.sale_date[df.sale_date.year == single_year].median())

#make a new column from just the years, add it to DF
df.loc[:,'year'] = df.loc[:,'sale_date'].dt.year

print(df.loc[df.store_name =='S5',:].groupby('year')['num_sold']
                            .median()
                            .reset_index()
                            .sort_values('num_sold',ascending=False)
                            .head(1))




# In[105]:


# 6.4 Which store recorded the highest number of sales for the largest number of days?

##select which store "won" on a single day
df.loc[df.sale_date == pd.Timestamp(start_date),:].sort_values('num_sold', ascending=False).head(1)
                                                
##iterate over all thedays
start_date = df.sale_date.sort_values()[0].date()
end_date = df.sale_date.sort_values().iloc[-1].date()
daterange = pd.date_range(start_date, end_date)
day_winner = pd.DataFrame()

for single_date in daterange:
    day_winner = day_winner.append( df.loc[df.sale_date == pd.Timestamp(single_date),:].sort_values('num_sold', ascending=False).head(1) )
#.reset_index()
#.sort_values('num_sold', ascending=False)
day_winner.store_name.value_counts().head(1)


# In[133]:


# 6.5 Which store ranks 5th in the cumulative number of units sold over the 3-year interval?
print(df.groupby('store_name')['num_sold'].sum().sort_values(ascending=False)[[4]])


# In[6]:


# 6.6 Your program should create a file named repaired.csv in the directory hw1/q4 which
# contains the same data as data.csv , but with “N/A” values replaced with the median
# sale of that store, over the entire 3-year interval. Retain the header row found in
# data.csv.
df2 = pd.read_csv("C:\\Users\\lauw02\\Desktop\\stats 418\\Stats-418-W20\\hw1\\q5\\data.csv")
df2.index=df2["Date"]
df_stores_only = df2[["S1","S2","S3","S4","S5","S6","S7","S8","S9","S10"]]

#df_stores_only


# In[11]:


for i in df_stores_only.columns:
    df2[i] = df2[i].fillna(df2[i].median())
    
df2[df_stores_only.columns].to_csv("C:\\Users\\lauw02\\Desktop\\stats 418\\Stats-418-W20\\hw1\\q5\\repaired.csv")

