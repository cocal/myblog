# -*- coding: utf-8 -*-

import os


dir_path = os.path.abspath('posts')

def titleManager():
    file_open = open('titles')
    try:
        titles = file_open.readlines();
    finally:
        file_open.close()
    return titles

##这块代码略奇葩 我还没理清楚怎么写 暂时就这样吧  - -
def initTitleManager():
    post_files = os.listdir(dir_path)
#     post_files = os.path.join(os.path.dirname(__file__),'posts')
    temp =''
    for filename in post_files:
        file_open = open(dir_path + '/' + filename)
        try:
            title = getContent(file_open.readline());
            if title == -1:
                continue;
            date = getContent(file_open.readline());
            temp = temp + date + ":" + title  +'\n' 
        finally:
            file_open.close()
            
    title_write = open('titles','w')
    try:
        title_write.write(temp);
        title_write.write("---------upate by -----\n")
    finally:
        title_write.close()
    return  temp

def getContent(line):
    line = line.strip('\n')
    tokens = line.split(':')
    if(len(tokens) > 1):
        return tokens[1]
    else: 
        return -1;
    

if __name__ == '__main__':
#     str = titleManager();
#     for x in str:
#         print x
    f = initTitleManager();
#     for x in f:
#         print x;
