#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from time import time
from IPython.display import display # Allows the use of display() for DataFrames
from matplotlib import pyplot as plt
# Import supplementary visualization code visuals.py

df= pd.read_csv(r"C:\Users\gsubh\Downloads\data.csv")
df1= pd.read_csv(r"C:\Users\gsubh\Downloads\data.csv")


# In[2]:


df.describe()


# In[3]:


df1['income']=df1['income'].replace(' <=50K',0)
df1['income']=df1['income'].replace(' >50K',1)
display(df1)


# ###  We are changing the values of the income to numerical values, inorder to get the correlation with the other features 

# In[4]:


correlationMatrix= df1.corr()
print(correlationMatrix)


# In[5]:


df1['income']=df1['income'].replace('0',0)
df1['income']=df1['income'].replace('1',1)
display(df1)


# In[6]:



import seaborn as sns
plt.figure(figsize=(14,14))
cor = df1.corr()
sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
plt.show()


# By observing the correlation map, we can that infer that income feature is not heavily/ fully dependent on any single feature. Also, fnlwgt is giving us the negative correlation with income. So, we might drop this columns going further.

# # EDA

# In[7]:


print("Number of Null Rows in Age Column is ", df1['age'].isna().sum())
sns.distplot(df['age'])


# Our data has a right skewness, with the majority of the ages lying between 20 and 50. As people get older, the number continues to decrease. We also see that the age field does not include any null values.

# ## Workclass column

# In[8]:


df1['workclass'].value_counts()
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.countplot(df1['workclass'])


# When we look at the unique values for workclass, we notice that there are seven different sorts of values, as well as some missing values denoted by a '?'. Null values account for 1836, or around 5% of the data.

# In[9]:


c=0
for index,row in df1.iterrows():     
    if row['workclass'].strip()=="?":
        display(row)
        c+=1
#print(c)


# We see that the majority of people work in the 'Private' sector.
# We also notice something interesting here: the values that are missing 'Workclass' are also missing 'Occupation'!

# ## Education column

# In[10]:


print(df1['education_level'].value_counts())
sns.set(rc={'figure.figsize':(18.7,8.27)})
sns.countplot(df1['education_level'])


# There are 16 different categories in the 'Education' column. The majority of these categories fall within the 'School' category (different classes are divided into multiple categories). There are no missing values in this column, and the majority of persons have a 'HS-grad' education level, followed by 'Some-college' and 'Bachelors'.

# # Visualizing the features against Income Column 

# ## Race vs Income

# In[11]:


import matplotlib.pyplot as plt
 

# count plot on two categorical variable
sns.countplot(x ='race', hue = "income", data = df)
 
# Show the plot
plt.show()


# In[12]:


sns.countplot(x ='workclass', hue = "income", data = df)
# Show the plot
plt.show()


# In[13]:


sns.countplot(x ='education_level', hue = "income", data = df)
# Show the plot
plt.show()


# In[14]:


sns.countplot(x ='relationship', hue = "income", data = df)
# Show the plot
plt.show()


# In[15]:


sns.scatterplot(x="age",y="hours-per-week",hue="income",data=df)
plt.show()


# # Analysis from Above Plots

# - If a person's race is 'White'/'Asian-pac-islander,' he or she has a good likelihood of earning more than 50K(Dollars).
# - Males are more likely than females to earn more than 50K(Dollars).
# - Number of People earning more than 50K is high in private sector when compared to Others. If Workclass is 'Self-emp-inc,' the percentage of those earning more than 50K(Dollars) is greater.
# - People with a 'Masters/Doctorate/Prof-school' education have a larger ratio of >50K earning than those with a '=50K' education. The ratio of =50K: >50K for bachelor's degrees is roughly 10:7.
# - If the relationship status is 'Husband/Wife,' the odds of earning more than 50K(Dollars) are considerable.
# - Based on the scatterplot of age, hours per week, and income, we can see that to make more than 50K(Dollars), a person must be at least 30 years old or he/she should work at least 60 hours per week.

# # Cleaning Data

# We have the missing Values in our data set for the columns workclass, occupation and native_country. So Instead of removing the rows with missing values we are going to replace them, with the mean/mode. Hence, we replace ‘?’ is ‘Workclass’ column by ‘Private’, ‘Occupation’ column by ‘Prof-speciality’ and ‘Native_country’ by ‘United_States’.

# In[16]:


df1['workclass']=df1['workclass'].replace(' ?',' Private')
df1['occupation']=df1['occupation'].replace(' ?',' Prof-specialty')
df1['native-country']=df1['native-country'].replace(' ?',' United-States')


# # Logically Combining the data to reduce number of Categories in Features

# In[17]:


print(df1['workclass'].value_counts())
print()
print(df1['education_level'].value_counts())


# We can keep Never-worked and Without-pay into one category. Also Group State-gov, Local-gov into Government. Add Self-emp-not-inc into ‘Private’ category 
# We combine all the columns relevant to schools in ‘School’ category, Lets keep ‘Doctorate’ and ‘Prof school’ in a single category ‘Doctorate’, ‘Assoc-acdm’ and ‘Assoc-voc’ in one category ‘Assoc’, and ‘HS-Grad’ and ‘Some-college’ in one category ‘College’.

# In[18]:


df1['workclass']=df1['workclass'].replace(' Never-worked',' Without-pay')
df1['workclass']=df1['workclass'].replace(' State-gov',' Government')
df1['workclass']=df1['workclass'].replace(' Local-gov',' Government')
df1['workclass']=df1['workclass'].replace(' Self-emp-not-inc',' Private')
print(df1['workclass'].value_counts())


# In[19]:


df1['education_level']=df1['education_level'].replace(' 1st-4th',' School')
df1['education_level']=df1['education_level'].replace(' 5th-6th',' School')
df1['education_level']=df1['education_level'].replace(' 7th-8th',' School')
df1['education_level']=df1['education_level'].replace(' 9th',' School')
df1['education_level']=df1['education_level'].replace(' 10th',' School')
df1['education_level']=df1['education_level'].replace(' 11th',' School')
df1['education_level']=df1['education_level'].replace(' 12th',' School')
df1['education_level']=df1['education_level'].replace(' Preschool',' School')
df1['education_level']=df1['education_level'].replace(' HS-grad',' College')
df1['education_level']=df1['education_level'].replace(' Some-college',' College')
df1['education_level']=df1['education_level'].replace(' Prof-school',' Doctorate')
df1['education_level']=df1['education_level'].replace(' Assoc-voc',' Associate')
df1['education_level']=df1['education_level'].replace(' Assoc-acdm',' Associate')
print(df1['education_level'].value_counts())


# In[20]:


df1['marital-status']=df1['marital-status'].replace(' Married-spouse-absent',' No spouse')
df1['marital-status']=df1['marital-status'].replace(' Separated',' No spouse')
df1['marital-status']=df1['marital-status'].replace(' Widowed',' No spouse')
df1['marital-status']=df1['marital-status'].replace(' Divorced',' No spouse')
df1['marital-status']=df1['marital-status'].replace(' Married-AF-spouse',' No spouse')

print(df1['marital-status'].value_counts())


# In[21]:


df1['relationship']=df1['relationship'].replace(' Own-child',' Other')
df1['relationship']=df1['relationship'].replace(' Unmarried',' Other')
df1['relationship']=df1['relationship'].replace(' Not-in-family',' Other')
df1['relationship']=df1['relationship'].replace(' Other-relative',' Other')
print(df1['relationship'].value_counts())


# In[22]:


df1['race']=df1['race'].replace(' Amer-Indian-Eskimo',' Other')
print(df1['race'].value_counts())


# # Encoding The Data

# In[23]:


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df1.drop(columns=['fnlwgt'])
df1.columns


# In[24]:


df1['workclass']=le.fit_transform(df1['workclass'])
df1['education_level']=le.fit_transform(df1['education_level'])
df1['marital-status']=le.fit_transform(df1['marital-status'])
df1['occupation']=le.fit_transform(df1['occupation'])
df1['relationship']=le.fit_transform(df1['relationship'])
df1['race']=le.fit_transform(df1['race'])
df1['sex']=le.fit_transform(df1['sex'])
df1['native-country']=le.fit_transform(df1['native-country'])


# In[25]:


print(df1)


# # Scaling Data

# In[26]:


from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
df1_x=df1.drop('income',axis='columns')
y=df1['income']
dataset=sc.fit_transform(df1_x)
x=pd.DataFrame(dataset,columns=df1_x.columns)

