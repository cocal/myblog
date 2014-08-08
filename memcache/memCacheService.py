# -*- coding: utf-8 -*-
'''
Created on 2014年8月4日

@author: cocal
'''
# 
#                                          +--------------+
#                                          |              |
# +-------------+                          |              |
# |             |                   LOCK   |              |
# |    APPLY    +------------------------> |              |
# |             |                          |   memCache   |
# +-------------+                          |              |
#                                          |              |
#                                          |              |
#                                          |              |
#                                          |              |
# +-------------+                          |    Service   |
# |             |  ULock                   |              |
# |    APPLY2   +--------------------------+              |
# |             |                          |              |
# +-------------+                          |              |
#                                          +--------------+


import MemCacheDto


__memCache__ = {'version':'version:0.001Beta'}

def viewAllCache():
    for item in __memCache__.keys():
        print __memCache__[item]

def lockItem(key):
    if __memCache__.has_key(key) :
        __memCache__[key] = __memCache__.get(key).lock()
        
        
def addCache(key,value,time = None):
    if __memCache__.has_key(key) :
        return 'the key is checked'
    m = MemCacheDto.memCache()
    m.key = key
    m.val = value
    m.lifeCycle = time
    __memCache__[key] = m
    
    