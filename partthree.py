
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error , r2_score
from sklearn.model_selection import train_test_split 

df = pd.read_csv(r"Downloads\delaney_solubility_with_descriptors.csv")
y = df['logS']
x = df.drop('logS' , axis = 1)

x_train , x_test , y_train , y_test = train_test_split(x, y, test_size =0.2, random_state = 100)
lr = LinearRegression()
lr.fit(x_train, y_train)
y_lr_train_pred = lr.predict(x_train)
y_lr_test_pred = lr.predict(x_test)
# y_train
# y_lr_train_pred

lr_train_mse = mean_squared_error(y_train, y_lr_train_pred)
lr_train_r2 = r2_score(y_train, y_lr_train_pred)

lr_test_mse = mean_squared_error(y_test, y_lr_test_pred)
lr_test_r2=r2_score(y_test,y_lr_test_pred)

# print(f"MLresultoflearn MSE (Train): ", lr_train_mse)
# print(f"LR MSE (Train): ", lr_train_r2)
# print(f"LR MSE (Train): ", lr_test_mse)
# print(f"LR MSE (Train): ", lr_test_r2)
lr_results = pd.DataFrame(['Linear regression',lr_train_mse, lr_train_r2, lr_test_mse , lr_test_r2]).transpose()
# give Discreptive Names To Columns
lr_results.columns = ['Method','Training MSE' , 'Training R2' , 'Test MSE' ,'Test R2']
lr_results


# In[30]:


df


# In[31]:


import matplotlib.pyplot as plt
import numpy as np
plt.scatter(x=y_train , y = y_lr_train_pred, c='#7CAE00' ,alpha = 0.3)
plt.plot(y_train,y_train, '#F8766D')
# To draw line use numpy


# In[32]:


plt.style.available