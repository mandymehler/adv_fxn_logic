#!/usr/bin/env python
# coding: utf-8

# In[2]:


l1 = [1, 2, [3, 4, [5, 6], 7, 8]]

def has_list(data): #use same function from while loop, this is our helper function to check if list contains any sublists
    for i in range(len(data)):
        if type(data[i]) == list:
            return True 
    return False 

def recursive_solve(data): #define function with parameter/argument
    if has_list(data) == False: #base case if has_list(data) returns false, it has NO sublists, only ints. This IS the STOP point. 
        for i in range(len(data)): #this is same function as while loop, replaces prior list 
            data[i] = data[i] + 1 #adds 1 to each element of inner most list
        return data #passes the modified inner most list to previous recursion level

    else: 
        for i in range(len(data)): #keep trying, recursive case
            if type(data[i]) == list: #if it finds a list
                return recursive_solve(data[i]) #it calls recursive_solve on that sublist

print(recursive_solve(l1)) #prints innermost list l1



# In[ ]:




