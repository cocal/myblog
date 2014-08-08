# -*- coding: utf-8 -*-
'''
Created on 2014年8月4日

@author: cocal
'''
import MemCacheDto


__memCache__ = {'version':'0.001Beta'}

def viewAllCache():
    print __memCache__

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
    
    