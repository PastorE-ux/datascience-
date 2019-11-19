#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sys 
bm = []

print('-------Menu------')
print('1-----Add Bookmarks')
print('2-----Edit Bookmarks')
print('3-----Delete Bookmarks')
print('4-----View Bookmarks')
print('5-----Exit')
while True:

    choose =input("Choose a Number: ")

    if choose == '1':
        ad_bm = input("Add Bookmark: ")
        bm.append(ad_bm)
        
    elif choose == '2':
        de_bm = input("Edit Bookmark: ")
        index=bm.index(de_bm)
        bm.remove(de_bm)
        ad_bm = input("New Bookmark: ")
        bm.insert(index,ad_bm)
        
    elif choose=='3':
        de_bm = input("Delete Bookmark: ")
        bm.remove(de_bm)

    elif choose =='4':
        print(bm)
        
    
    elif choose == '5':
        sys.exit()


# In[ ]:




