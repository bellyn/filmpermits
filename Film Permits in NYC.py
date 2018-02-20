
# coding: utf-8

# <h3> Film Permits in NYC</h3>

# I am interested in looking at the most-filmed neighborhoods in NYC. To do this, I will be looking at the film permits issued between 2012 - 2017.

# <h3>The Preliminaries</h3>

# In[1]:


import pandas as pd
import numpy as np
df = pd.read_csv("Film_Permits.csv")
df.info()


# <h3>Data Cleaning</h3> 
# In this step I am getting rid of the columns unnecessary for this analysis, such as EventAgency, Country, CommunityBoard, PolicePrecinct

# In[2]:


df = df.sort_values(df.columns[0], ascending="True") ## sort by EventId
df = df.reset_index(drop=True)
df = df.drop(["EventAgency","CommunityBoard(s)","PolicePrecinct(s)","Country"], axis=1) ## drop the unused categories


# In[11]:


df.columns = ['id','event','start','end','enteredon','parkingheld','borough','category','subcategory','zipcode']
df.head(5)


# In[4]:


#df1 = df.assign(**{'zipcode':df['zipcode'].str.split(',')})


# In[5]:


#df1.zipcode = df.zipcode.astype(int)
#df1.dtypes


# In[7]:


#df.zipcode = map(int, df.zipcode)
df2 = pd.DataFrame(df.zipcode.str.split(',').tolist()) # split by comma and create new rows
df2 = df2.reset_index()[[0, 'id']] # reset index and remove invalid row 
#df2.columns = ['zipcode', 'id'] # rename columns
#df2 = df2[['id', 'zipcode']] # reorder columns to match df1
#df2

#df3 = pd.merge(df2, df1, left_on='id', right_on='id', suffixes=('', '_original')) # Left join df1 and df2 on id

#print(df1)
#print(df2)
#print(df3)


# In[13]:


x = float (1)
df1 = pd.DataFrame({'id': ['a', 'b', 'c'],
'neighbourhood': ['harlem', 'soho', 'manhattan'],
'residents': [x, 12342, 12433],
'zipcode': ['3000', '4000,4003', '3333,2222,3311']})

df2 = pd.DataFrame(df1.zipcode.str.split(',').tolist(), index=df1.id).stack() # split by comma and create new rows
print(df2)
df2 = df2.reset_index()[[0, 'id']] # reset index and remove invalid row 
df2.columns = ['zipcode', 'id'] # rename columns
df2 = df2[['id', 'zipcode']] # reorder columns to match df1


df3 = pd.merge(df2, df1, left_on='id', right_on='id', suffixes=('', '_original')) # Left join df1 and df2 on id

print(df1)
print(df2)
print(df3)

