#!/usr/bin/env python
# coding: utf-8

# In[1]:


from itertools import combinations
def build_combination(n,k):
    result = combinations(range(n),k)
    return result

if __name__ == '__main__':
    #以下为针对模块的测试信息
    a = build_combination(4, 3)
    for i in a:
        print(i)

