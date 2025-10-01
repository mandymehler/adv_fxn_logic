#!/usr/bin/env python
# coding: utf-8

# In[2]:


def thresh(input_list, x): #create fxn with 2 arguments (input list, threshold value)
    result = []  # create an empty list to store filtered elements
    for val in input_list: #iterates over values in input list
        if val <= x: #if value is less than or equal to 6
            result.append(item)  #will add value to blank result list above
    return result #gives the new list result

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

answer = thresh(input_list, 6) #calls the function
print(answer)  

