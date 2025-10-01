#!/usr/bin/env python
# coding: utf-8

# In[2]:


l1 = [1,2,3,4,[5,6,7,[8,9]]]
def has_list(data): #define function with argument (list)
    for i in range(len(data)): #interating through list index's
        if type(data[i]) == list: # if the type of value at index i is a list
            return True #this will return new l1 to while loop 
    return False #this will run until only integers, this is our stopping point so loop won't be infinite

while has_list(l1): #calls the function above with l1 to while loop, it will keep running until has_list is true
    for i in range(len(l1)): #iterating through list 
        if type(l1[i]) == list: #if type is list, exits if false and goes to for loop
            l1 = l1[i] #if true, reassigns l1, we do lose original value here, l1 is now a sublist
            break #breaks out of inner for loop after if finds list and reassigns,  
                    #then the while condition is checked again and the process repeats until no list is found.

for i in range(len(l1)): #iterating through innermost sublist, l1 has been modfied due to while loop stopping when all elements are not a list
    l1[i] = l1[i] + 1 #adding 1 to each value of innermost sublist

print(l1)  


# In[ ]:




