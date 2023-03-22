#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Functions


# In[2]:


def test():
    print("this is my first function")


# In[3]:


test()


# In[4]:


type(test)


# In[5]:


type(test())


# In[6]:


def test1  ():
    return "this is my first function"


# In[7]:


test1() + " vish "


# In[8]:


type(test1())


# In[9]:


def test3():
    return 1,3,5,[1,2,6,5]


# In[10]:


test3()


# In[11]:


a=test3()


# In[12]:


a


# In[13]:


a,b,c =(23,45,67)


# In[14]:


a


# In[15]:


b


# In[16]:


c


# In[17]:


a,b,c,d =test3()


# In[18]:


a


# In[19]:


b


# In[20]:


c


# In[21]:


d


# In[22]:


def test4():
    a=4*5
    b=6+4
    return a,b


# In[23]:


test4()


# In[24]:


g=test4()


# In[25]:


g


# In[26]:


j,k=test4()


# In[27]:


j


# In[28]:


k


# In[29]:


_ , v = test4()


# In[30]:


_


# In[31]:


test3()


# In[32]:


_ , _ , _ ,p =test3()


# In[33]:


_


# In[34]:


_


# In[35]:


p


# In[36]:


a = 1
b= 10
while a<=b :
    print(a)
    a=a+2
else :
    print("print this else block")


# In[37]:


def test5():
    a=1
    b=10
    while a<=b:
        print(a)
        a=a+2
    else :
        print("print this else block")
    


# In[38]:


test5()


# In[39]:


def test5(a,b):
    while a<=b:
        print(a)
        a=a+2
    else :
        print("print this else block")


# In[40]:


test5(a,b)


# In[41]:


def test6(a,b):
    while a<=b:
        print(a)
        a=a+2
    else :
        print("print this else block")


# In[42]:


test6(1,8)


# In[43]:


test6(54,99)


# In[44]:


def test6(a,b):
    while a<=b:
        print(a)
        return a
        a=a+2
    else :
        print("print this else block")


# In[45]:


test6(1,10)


# In[46]:


def test5(a,b):
    l=[]
    while a<=b:
        #print(a)
        l.append(a)
        a=a+2
    else :
        print("print this else block")
    return l


# In[47]:


test5(1,10)


# In[48]:


def test(a,b):
    """this is my function for concantination or addition"""
    return a+b
    


# In[49]:


test(1,10)


# In[50]:


test("vishwa", "patil")


# In[51]:


test(a=8,b=5)


# In[52]:


def test1(a,b,c,d,e):
    return a,b,c,d,e


# In[53]:


test1(3,4,5,6,7)


# In[54]:


def test(*a):
    return a


# In[55]:


test(2,56)


# In[56]:


test(3,5,"gh",["gh,3,6"])


# In[57]:


def test4(*args):
    return args


# In[58]:


test4(45,67,89,56)


# In[59]:


def test5(*a):
    l=[]
    for i in a:
        l.append(i)
    return l
        


# In[60]:


test5(3,5,7,89,45,"ug")


# In[61]:


def test6(a,b,c,d, *m):
    return a,b,c,d,m


# In[62]:


test6(3,4,5,6,7,8,9)


# In[63]:


def test7(*m,a,b,c,d,e):
    return m,a,b,c,d,e


# In[64]:


test7(4,5,6,7,23,a=8,b=4,c=34,d=56,e=78)


# In[65]:


def test8(**kwargs):
    return kwargs


# In[66]:


test8(a=3,b=5,c=7,d=8)


# In[71]:


d={'a': 3, 'b': 5, 'c': 7, 'd': 8}


# In[72]:


test8(d)


# In[73]:


def test9(*m, **v):
    return m , v
    


# In[74]:


test9(345,56,78,93,78,89,b=8,c=1,d=4,g=56)


# In[75]:


def test10(*m):
    n=1
    for i in m:
        if type(i)==int:
            n=n+i
    return n


# In[76]:


test10(2,3,4,5,6)


# In[77]:


def test1(*m):
    n=1
    for i in m:
        if type(i)==int:
            n=n*i
    return n


# In[78]:


test1(2,3,4,5,6)


# In[79]:


n=lambda a,b :a+b 


# In[80]:


n(4,5)


# In[81]:


def test(a,b):
    return a+ b


# In[82]:


test(4,5)


# In[83]:


n(8,9)


# In[84]:


b=lambda *vish : vish


# In[85]:


b(4,5,6,7,8,9,6)


# In[86]:


t=(3,4,4,5,5,6,78,67,7,77)
l=[]
for i in t:
    l.append(i)


# In[87]:


l


# In[88]:


[i for i in t]


# In[89]:


v= "vish"


# In[90]:


[i for i in v]


# In[91]:


[i*i for i in range(10)]


# In[92]:


l=[]
for i in range(10):
    l.append(i*i)


# In[93]:


l


# In[96]:


l = lambda *X : [i**2 for i in X]


# In[98]:


l(4,5,6,6,7,8,9)


# In[101]:


test14(a=7,b="vish",c=56,d="vish",l=[1,2,4,6,"vish"])


# In[104]:


def test14(**kwargs):
    count = 0
    print(kwargs)
    print(kwargs.values())
    for v in kwargs.values():
        if type(v) == str or type(v) == list:
            count+=1
    return count


# In[106]:


test14(a=7,b="vish",c=56,d="vish",l=[1,2,4,6,"vish"])


# In[107]:


def test15(**kwargs):
    return list(kwargs.values())


# In[108]:


test15(a=7,b="vish",c=56,d="vish",l=[1,2,4,6,"vish"])


# In[ ]:




