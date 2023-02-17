#!/usr/bin/env python
# coding: utf-8

# # Project Overview 
# ### For this project, we will be analyzing a dataset containing information about "Bike Sharing programs" in various cities.
# ### Our goal is to analyze this data to gain insights into bike usage patterns and make recommendations for improving bike-sharing programs.

# #### 1- Load the dataset into a dataframe

# In[1]:


import pandas as pd

bike_df = pd.read_csv(r'C:\Users\ZZZ\Downloads\day.csv')


# #### 2- Drop irrelevant columns

# In[2]:


bike_df.drop(['instant', 'dteday', 'casual', 'registered'], axis=1, inplace=True)


# #### 3- Rename columns

# In[3]:


bike_df.rename(columns={'yr': 'year', 'mnth': 'month', 'holiday': 'is_holiday',
                        'weekday': 'day_of_week', 'workingday': 'is_workingday',
                        'weathersit': 'weather_condition', 'temp': 'temperature',
                        'atemp': 'feels_like_temp', 'hum': 'humidity', 'windspeed': 'wind_speed',
                        'cnt': 'total_rentals'}, inplace=True)


# #### 4- Convert data types

# In[5]:


bike_df['year'] = bike_df['year'].astype('category')
bike_df['month'] = bike_df['month'].astype('category')
bike_df['day_of_week'] = bike_df['day_of_week'].astype('category')
bike_df['is_holiday'] = bike_df['is_holiday'].astype('bool')
bike_df['is_workingday'] = bike_df['is_workingday'].astype('bool')
bike_df['weather_condition'] = bike_df['weather_condition'].astype('category')


# ### Visualization Step

# In[6]:


import matplotlib.pyplot as plt
import seaborn as sns


# #### 5- Visualize total rentals by year

# In[7]:


sns.barplot(x='year', y='total_rentals', data=bike_df)
plt.title('Total Rentals by Year')
plt.show()


# #### 6- Visualize total rentals by month

# In[8]:


sns.barplot(x='day_of_week', y='total_rentals', data=bike_df)
plt.title('Total Rentals by Day of Week')
plt.show()


# #### 7- Visualize total rentals by weather condition

# In[9]:


sns.barplot(x='weather_condition', y='total_rentals', data=bike_df)
plt.title('Total Rentals by Weather Condition')
plt.show()


# #### 8- Correlation Heatmap

# In[11]:


sns.heatmap(bike_df.corr(), annot=True)
plt.title('Correlation Heatmap')
plt.show()


# #### 9- Visualize total rentals by month

# In[12]:


sns.barplot(x='month', y='total_rentals', data=bike_df)
plt.title('Total Rentals by Month')
plt.show()


# #### 10- Visualize the distribution of total rentals

# In[13]:


sns.histplot(x='total_rentals', data=bike_df, kde=True)
plt.title('Distribution of Total Rentals')
plt.show()


# ## Conclusion

# ### Based on our analysis and model, we can make the following recommendations for improving bike-sharing programs:

# ### 1- Increase bike availability during the summer months, when demand is highest.

# ### 2- Offer discounts or promotions during the weekdays, when demand is lower.

# In[ ]:




