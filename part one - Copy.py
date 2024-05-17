#!/usr/bin/env python
# coding: utf-8

# # Project: Investigate medical students dataset

# ## introduction

# # Description About Dataset
# 

# ### medical students dataset is a community built medical students dataset.This data set contains information about 20,000 medical student collected from medical students dataset. it includes 20,000 rows and 13 columns. Thorugh medical students dataset investigation different packages are used (pandas, numpy, matplotlib).
# 
# ### Before the analysis of the dataset, data wrangling phase has been conducted to clean the data from unimportant columns, noisy data, and other problems. Before data wrangling phase, general properities about the dataset has been addressed.

# ### questions that is analyized in the dataset: 
# 
# #### 1- Information about students who has diabates
# #### 2- Count smoking students 
# #### 3- Correlation between Height	and Weight and BMI
# #### 4- Show how blood preasure vary between smokers and non-smokers
# #### 5- Show the distribution of female and male numbers in each blood type
# #### 6- The number of people with diabetes and smoke at the same time
# #### 7- Information about students' heart rate depending on Gender 
# #### 8- How effected is the Cholesterol level by the weight
# #### 9- Information about stodents' temperatures
# #### 10- weight graph by age distribution 

# In[1]:


# import packages to use
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn-v0_8-dark')


# ## the database before cleaning

# ## Data Wrangling

# ### General Properties

# In[2]:


# Load csv file named medical_students_dataset.csv into data frame DF
df = pd.read_csv(r"C:\Users\Hany Alrashidy\OneDrive\Desktop\medical_students_dataset.csv")

# dimensions of DF
print("Dimensions of DF: ", df.shape)

# print Information of DF
print("\nInformation about DF: ")
print(df.info())

# First ten rows of DF
print("\nHead of DF: \n", df.head(10))


# In[3]:


df.set_index("Student ID", inplace = True)


# ## Data Cleaning
# ### fixing or removing incorrect, duplicate,noisy, or incomplete data within a dataset.
# # ______________________________________________________________
# ### Problems With the dataset
# #### 1: Remove unused Columns (if exist)
# #### 2: Remove duplication in the rows (check and process if exist)
# #### 3: Remove rows contains noisy data (Some movies has 'zero' budget or revenue. So, we need to discard it)
# #### 4: Check NN values and modify it with a value (zero or mean or median or stay as it is according to the data) 

# ## 1: Remove unused Columns (if exist)
# ### we don't have any unused columns
# ## 2: Remove duplication in the rows (check and process if exist)
# 

# In[4]:


# Number of rows (in advance)
print("Number of rows BEFORE removing duplicates:  ", df.shape[0])
# check Rows Duplication
duplicated_rows = sum(df.duplicated())
print("Duplicated rows to remove:                  ", duplicated_rows)
if(duplicated_rows):
    df.drop_duplicates(keep ='first', inplace=True)
print("Number of rows AFTER Removing duplication:  ", df.shape[0])


# ## 3- Remove rows contains noisy data (Some student has 'zero' Height or Weight or BMI or Temperature or Heart Rate or Blood Pressure or Cholesterol)

# In[5]:


"""Number of Rows before removing rows contains zero value in  'zero'Height or Weight or
BMI or Temperature or Heart Rate or Blood Pressure or Cholesterol columns"""
print("Number of rows before removing noisy data: ", df.shape[0])

# drop rows where value of a 'Height' column is zero
df.drop(df.index[df['Height'] == 0], inplace = True)

# drop rows where value of a 'Weight' column is zero
df.drop(df.index[df['Weight'] == 0], inplace = True)

# drop rows where value of a 'Temperature' column is zero
df.drop(df.index[df['Temperature'] == 0], inplace = True)

# drop rows where value of a 'Heart Rate' column is zero
df.drop(df.index[df['Heart_Rate'] == 0], inplace = True)

# drop rows where value of a 'Blood Pressure' column is zero
df.drop(df.index[df['Blood_Pressure'] == 0], inplace = True)

# drop rows where value of a 'Cholesterol' column is zero
df.drop(df.index[df['Cholesterol'] == 0], inplace = True)

"""Number of Rows after removing rows contains zero value in  'zero'Height or Weight or
BMI or Temperature or Heart Rate or Blood Pressure or Cholesterol columns"""
print("Number of rows after removing noisy data: ", df.shape[0])


# ## 4- Check NN values and modify it with a value (zero or mean or median or stay as it is according to the data)

# In[6]:


# Display all information about columns on the dataset
df.info()


# ### Using info function on DF, all columns has nulls
# #### but only afew of them impacts our data will give them the mean value (BMI, Height and weight) 

# In[7]:


# Calculate the mean of the 'BMI' column (excluding NaN values)
mean_bmi = df['BMI'].mean()

# Fill NaN values in the 'BMI' column with the calculated mean
df['BMI'].fillna(mean_bmi, inplace=True)


# In[8]:


# Calculate the mean of the 'Height' column (excluding NaN values)
mean_Height = df['Height'].mean()

# Fill NaN values in the 'Height' column with the calculated mean
df['Height'].fillna(mean_Height, inplace=True)


# In[9]:


# Calculate the mean of the 'Weight' column (excluding NaN values)
mean_Weight = df['Weight'].mean()

# Fill NaN values in the 'Weight' column with the calculated mean
df['Weight'].fillna(mean_Weight, inplace=True)


# ## Exploratory Data Analysis
# ### Descriptive statistics about DF

# In[10]:


#descriptive statistics
df.describe()

