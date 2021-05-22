#!/usr/bin/env python
# coding: utf-8

# ## Netflix Data Analytics

# In[2]:


## Import the necessary library

import pandas as pd
import seaborn as sns


# In[19]:


# Import the dataset

Netflix = pd.read_csv('C:/Users/User/Downloads/Netflix.csv')


# In[20]:


Netflix.head(2)


# In[21]:


Netflix.info()


# In[22]:


Netflix.shape


# ## Task.1. Is there any Duplicate Record in this dataset ? If yes, then remove the duplicate records.

# In[26]:


## using duplicate function

Netflix.duplicated().sum()


# In[29]:


Netflix = Netflix.drop_duplicates()


# In[30]:


Netflix.duplicated().sum()


# #### Previously we have 7789 rows no we have 7787 rows that means we have sucessfully removed the duplicate values.

# ## Task.2. Is there any Null Value present in any column ? Show with Heat-map.

# In[32]:


## Checking for null value

Netflix.isnull().sum()


# In[36]:


## Drawing a heat map

sns.heatmap(Netflix.isnull(), cbar= False)


# ## Q.1. For 'House of Cards', what is the Show Id and Who is the Director of this show ?
# 

# In[37]:


Netflix.head(2)


# In[39]:


Netflix[Netflix['Title'].isin(['House of Cards'])]


# ## Q.2. In which year highest number of the TV Shows & Movies were released ? Show with Bar Graph.

# In[40]:


## Let's type the dtypes of all the columns

Netflix.dtypes


# In[41]:


## As we see that Release_Data is in string form so we need to convert the string into datetime.


# In[43]:


## We first create a new column

Netflix['Date_N'] = pd.to_datetime(Netflix['Release_Date'])


# In[44]:


Netflix.dtypes


# In[45]:


Netflix.head()


# In[46]:


## Les count the year using value_counts()


# In[51]:


Netflix['Date_N'].dt.year.value_counts()


# In[52]:


## Let's draw a barchart


# In[53]:


Netflix['Date_N'].dt.year.value_counts().plot(kind = 'bar')


# ##  Q.3. How many Movies & TV Shows are in the dataset ? Show with Bar Graph.

# In[54]:


Netflix['Category'].value_counts()


# In[55]:


Netflix['Category'].value_counts().plot(kind = 'bar')


# ## Q.4. Show all the Movies that were released in year 2000.

# In[61]:


## Let's create new year column

Netflix['year'] = Netflix['Date_N'].dt.year


# In[59]:


Netflix.head(2)


# In[63]:


## Lets do the filtering

Netflix[(Netflix.Category == 'Movie') & (Netflix.year == 2020)]


# ## Q.5. Show only the Titles of all TV Shows that were released in India only.

# In[70]:


Netflix['Title'][(Netflix.Category == 'TV Show') & (Netflix.Country == 'India')]


# ## Q.6. Show Top 10 Directors, who gave the highest number of TV Shows & Movies to Netflix ?

# In[69]:


Netflix['Director'].value_counts().head(10)


# ## Q.7. Show all the Records, where "Category is Movie and Type is Comedies" or "Country is United Kingdom".

# In[75]:


Netflix[(Netflix.Category == "Movie") & (Netflix.Type == "Comedies") | (Netflix.Country == 'United Kingdom')]


# ## Q.8. In how many movies/shows, Tom Cruise was cast ?

# In[76]:


Netflix.head(2)


# In[79]:


## To find whether or not a particular string exist in the given column we need to use str.contains()

Netflix[Netflix['Cast'].str.contains('Tom Cruise')]


# In[80]:


## To fix this error we have to Just a friendly reminder thatove the null values in the cast column

#Checking for null values

Netflix['Cast'].isnull().sum()


# In[81]:


## Let's create a new dataframe by dropping all the null values in the older dataframe

New_netflix = Netflix.dropna()


# In[83]:


New_netflix.isnull().sum()


# #### Their is no single null values in the data

# In[84]:


## Lets repeat the previous command

New_netflix[New_netflix['Cast'].str.contains('Tom Cruise')]


# ## Q.9. What are the different Ratings defined by Netflix ?

# In[92]:


Netflix['Rating'].value_counts()


# ## Q.9.1. How many Movies got the 'TV-14' rating, in Canada ?

# In[103]:


Netflix[Netflix.Rating == 'TV-14']


# In[105]:


Netflix['Duration'].max()


# ## How can we sort the dataset by Year ?

# In[106]:


Netflix.sort_values(by='year',ascending = False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




