#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Simple Python Regression Code

# Training data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Calculate slope (m)
m = (y[-1] - y[0]) / (x[-1] - x[0])

# Calculate intercept (b)
b = y[0] - m * x[0]

# Predict value for x = 6
x_new = 6
y_pred = m * x_new + b

# Print result
print("Predicted value:", y_pred)


# In[ ]:




