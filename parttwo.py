
# In[11]:


# Load csv file named medical_students_dataset.csv into data frame DF
df2 = pd.read_csv(r"C:\Users\Hany Alrashidy\OneDrive\Desktop\medical_students_dataset - plt.csv")
df2= df2[['Height', 'Weight' , 'BMI']]
df = pd.read_csv(r"C:\Users\Hany Alrashidy\OneDrive\Desktop\medical_students_dataset.csv")
df2.boxplot()
plt.show()
# ### Add 


# ## From the above result, we get some important insights:
# 
# ####  1- Minimum heart rate = 60, average = 79.510192, and maximum = 99
# ####  2- Youngest student is 18 year old and the oldest is 34 year old  
# ####  3- The mean and the median in all columns are almost the same which leads to a normal distributions
# ####  4- Minimum BMI = 10.074837, average = 23.34013, and maximum = 44.355113
# ####  5- Students bodys' temperature is between 96 and 101 around 98 as a mean
# ####  6- Blood Pressure Ranges from 90 to 139

# ## Research Question 1:  Information about students who has Diabetes

# In[12]:


yes = df[df["Diabetes"] == 'Yes'].shape[0]
print("Number of yes :", yes)
no = df[df["Diabetes"] == 'No'].shape[0]
print("Number of no :", no)
NaN= df['Diabetes'].isna().sum()
print("Number of not answered or empty :", NaN)

# Values for the pie chart
values = [yes, no, NaN]

# Labels for each value
labels = ['Yes', 'No', 'NaN']

# Creating the pie chart
plt.figure(figsize=(8, 6))  # Adjust the figure size if needed
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart of Variables')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

plt.show()


# ## Research Question 2:  count smoking students 

# In[13]:


# count each how many of each age of smokes
ages=[18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34]
for i in ages:
    years_old_number= df[df["Age"] == i].shape[0]
    years_old_df= df[df["Age"] == i]
    year_smoking= years_old_df[years_old_df["Smoking"] == 'Yes'].shape[0]
    print("out of ",years_old_number, ' student that is ', i ,' years old' , year_smoking ,' of them smokes' ) 

#count the yes answers
yes = df[df["Smoking"] == 'Yes'].shape[0]
print("Number of yes :", yes)

#count the no answers
no = df[df["Smoking"] == 'No'].shape[0]
print("Number of no :", no)

#count the un-answered or empty
NaN= df['Smoking'].isna().sum()
print("Number of not answered or empty :", NaN)


# ### total number of smoking students and non-smoking

# In[34]:


# X-axis positions for the bars
x_values = [1, 2,3]

# Heights of the bars
heights = [yes, no, NaN]

# Labels for the bars
labels = ['Yes', 'No' , 'NaN']

# Creating a bar plot
# plt.bar(x_values, heights, tick_label=labels, color=['green', 'red', 'black'])
plt.scatter(x_values , labels)
plt.xlabel('choice')
plt.ylabel('Values')
plt.title('smokers servey result')
plt.show()



# ## Research Question 3:  Correlation between Height, Weight and BMI

# In[21]:


# construct df_ from three columns of the DF (Height, Weight and BMI)
df2 = pd.read_csv(r"C:\Users\Hany Alrashidy\OneDrive\Desktop\medical_students_dataset - plt.csv")
df2= df2[['Height', 'Weight' , 'BMI']]

# compute correlation using pearson correlation cofficient
corr_mat=df2.corr(method='pearson')

#draw the heatmap
sns.heatmap(corr_mat, cmap='viridis' , annot = True)
#set title
plt.title("Correlation matrix for Height, Weight and BMI")
# show plot
plt.show()


# ## From the above Heatmap: correlation is computed for each two variable: There  is a string positive correlation between Weight and BMI(0.84). There is weak negative correlation between BMI and Height. in addition there is a negative correlation between weight and height.

# ## Research Question 4: show how blood pressure vary between smokers and non-smokers

# In[22]:


plt.figure(figsize=(8, 6))
sns.boxplot(x='Smoking', y='Blood_Pressure', data=df)
plt.xlabel('Smoking')
plt.ylabel('Blood Pressure')
plt.title('Blood Pressure Distribution between Smokers and Non-Smokers')
plt.show()


# ### from this graph, we understand that smoking doesn't effect the Blood Pressure alot. However, smoking is not good for your health

# ## Research Question 5: show the distribution of female and male numbers in each blood type 

# In[23]:


# Crosstab to count the frequency of each combination of Blood Type and Gender
cross_tab = pd.crosstab(df['Blood_Type'], df['Gender'])

# Bar plot to visualize the relationship between Blood Type and Gender
cross_tab.plot(kind='bar', figsize=(8, 6))
plt.xlabel('Blood Type')
plt.ylabel('Count')
plt.title('Distribution of Blood Type by Gender')
plt.xticks(rotation=0)  # Rotate x-axis labels for better readability
plt.legend(title='Gender')
plt.show()


# ### in this graph, we see that numbers of females that has the blood type B or O is more that males. However, males has more A and AB blood type other than females

# ## Research Question 6: The number of people with diabetes and smoke at the same time

# In[24]:


# Count the number of students with diabetes
diabetes_count = df[df['Diabetes'] == 'Yes'].shape[0]
print("Number of students with diabetes:", diabetes_count)

# Count the number of student smoking
Smoking_count = df[df['Smoking'] == 'Yes'].shape[0]
print("Number of students who smokes:", Smoking_count)

# Count the number of student with diabetes and smoking at the same time
diabetes_and_smoke_count = df[(df['Diabetes'] == 'Yes') & (df['Smoking'] == 'Yes')].shape[0]
print("Number of people with diabetes and smoke at the same time:", diabetes_and_smoke_count)

# X-axis positions for the bars
x_values = [1, 2,3]

# Heights of the bars
heights = [diabetes_count, Smoking_count, diabetes_and_smoke_count]

# Labels for the bars
labels = ['has diabets', 'smokes' , 'has diabetes and smokes']

# Creating a bar plot
plt.bar(x_values, heights, tick_label=labels, color=['blue', 'red', 'purple'])
plt.xlabel('single choices and the intersection')
plt.ylabel('Values')
plt.title('intersection count')
plt.show()


# ## Research Question 7: information about students' heart rate depending on Gender 

# In[25]:


plt.figure(figsize=(8, 6))
sns.boxplot(data=df[df['Gender'] == 'Female'], x='Gender', y='Heart_Rate')
plt.title('Boxplot for Female Heart Rate')
plt.xlabel('Gender')
plt.ylabel('Heart Rate')
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(data=df[df['Gender'] == 'Male'], x='Gender', y='Heart_Rate')
plt.title('Boxplot for Female Heart Rate')
plt.xlabel('Gender')
plt.ylabel('Heart Rate')
plt.show()


# ### As we notice here, famales' heart rate is slightly higher that mens' heart rate 

# ## Research Question 8: How effected is the Cholesterol level by the weight

# In[26]:


# Calculate the correlation between Weight and Cholesterol
df2 = pd.read_csv(r"C:\Users\Hany Alrashidy\OneDrive\Desktop\medical_students_dataset - plt.csv")
correlation = df2['Weight'].corr(df2['Cholesterol'])

print(f"Correlation between Weight and Cholesterol: {correlation}")

# Create a scatter plot for Weight vs Cholesterol
plt.figure(figsize=(8, 6))
plt.scatter(df2['Weight'], df2['Cholesterol'])
plt.xlabel('Weight')
plt.ylabel('Cholesterol')
plt.title('Scatter Plot: Weight vs Cholesterol')
plt.grid(True)
plt.show()


# ### according to our dataset the correlation between the weight and the cholesterol level is weak nagative relation which means High cholesterol can affect anyone, regardless of their weight.However, having excess body weight can lead to increased cholesterol levels in normal medical cases

# ## Research Question 9: information about stodents' temperatures

# In[27]:


# Create a histogram for students' temperatures frequencies
plt.figure(figsize=(8, 6))
plt.hist(df['Temperature'], bins=50, color='red', edgecolor='red')
plt.xlabel('Temperature')
plt.ylabel('Frequency')
plt.title('Histogram of Students\' Temperatures')
plt.grid(True)
plt.show()


# In[ ]:





# In[28]:


# import packages to use
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn-v0_8-dark')
df2 = pd.read_csv(r"C:\Users\Hany Alrashidy\OneDrive\Desktop\medical_students_dataset - plt.csv") 
plt.figure(figsize=(8, 6))
plt.plot(df2['Age'], df2['Weight'], marker='*', linestyle='-')
plt.xlabel('Age')
plt.ylabel('Weight')
plt.title('Weight by Age')
plt.grid(True)
plt.show()


# # Conclusions
# ### This dataset is very rich in information. Some limitations the dataset contains are null and zero values in some features. These zero and null values hinders the analysis and have to be removed or treated. For example null values is an obstacle which stopped me when I was analyzing the counts. Furthermore zero values creates false results during the correlation plots and computing the pearson correlation between Height, Weight and BMI. there are a number of student who smokes which is bad for a student in such a young age. Finally there is a positive correlation between some of the features of the midical student dataset but we also have negative ones.
# 
# ### After the Exploratort Data Analysis we can conclude that:
# 
# ####  1- Minimum heart rate = 60, average = 79.510192, and maximum = 99
# ####  2- Youngest student is 18 year old and the oldest is 34 year old  
# ####  3- The mean and the median in all columns are almost the same which leads to a normal distributions
# ####  4- Minimum BMI = 10.074837, average = 23.34013, and maximum = 44.355113
# ####  5- Students bodys' temperature is between 96 and 101 around 98 as a mean
# #### 6- most of the students are non-smokers
# #### 7- most of the students don't have diabetes
# #### 10- There is a strong positive relation between weight and BMI
# #### 11- the smoking habbit is more common in 28-year-old  students