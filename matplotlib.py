#!/usr/bin/env python
# coding: utf-8

# In[1]:


i=1
while i<=10:
    
    print(i,i*i)
    i+=1


# In[2]:


i=1
while i<=30:
    print(i*10)
    i+=1


# In[3]:


i=105
while i>=7:
    print(i,end="  ")
    i=i-7
    


# In[4]:


i=10
while i>=1:
    print(i)
    i=i-1
    


# In[5]:


i=105
while i>=7:
    print(i,end="  ")
    i=i-7
    


# In[6]:


n=10
while n>=1:
    print(n*(n+1))
    break
    


# In[7]:


n=10
while n>=1:
    print(n*(n+1))
    break


# In[8]:


i=2 
sum=0
while i <=20:
    sum=sum+i
    i=i+2
print(sum)
    


# In[9]:



val=int(input())
i=1
while i<=20:
    print(f'{val}*{i}={val*i}')
    i+=1


# In[ ]:





# In[10]:


n=5
for i in range(5):
    for j in range(n):
        print('*',end=" ")
    print()


# In[11]:


n=5
for i in range(5,0,-1):
    print('*'*i)


# In[12]:


n=5
for i in range(5,0,1):
    print('*')


# In[13]:


n=5
for i in range(n):
    for j in range(n):
        print()


# In[14]:


for i in range(5):
    for j in range(5):
        if i==j or  j==i:
            print('*',end=' ')
    print()


# In[15]:


for i in range(1,5):
    for j in range(1,5):
        if i==n-1 or  j==n-1:
            print('*',end=' ')
        else:
            print('-',end=' ')
    print()


# In[16]:


lst=["hoao","uu","uhiuiuy"]
lst.append("hjhj")
lst


# In[17]:


lst.extend("jhkhu")


# In[18]:


lst


# In[19]:


class Item:
    def calculate_total_price(self,X,Y):
        return X*Y

item1 =Item()
item1.name="phone"
item1.price=100
item1.quantity=5
print(item1.calculate_total_price(item1.price,item1.quantity))

item2 =Item()
item2.name="Laptop"
item2.price=10000
item2.quantity=3



# In[20]:


s = "heLLo BuDdY"
s2 = s.title()
print(s2)


# In[21]:


class Person(object):
 
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
 
    def display(self):
        print(self.name)
        print(self.idnumber)
         
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
     
# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
 
        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
         
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))
 
 
# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")
a.display()
a.details()


# In[22]:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)
        print(self.age)

class Employee(Person):
    def __init__(self, name, age, salary, post):
        super().__init__(name, age)
        self.salary = salary
        self.post = post

    def show(self):
        print(f"EMP_name of person: {self.name}")
        print(f"EMP_age of person: {self.age}")
        print(f"Employee salary: {self.salary}")
        print(f"Employee post: {self.post}")

obj = Employee('gjjj', 25, 654545, "HR")

obj.show()


# In[23]:


n=list[3,3]


# In[24]:


n


# In[25]:


n=input(list[3,4])


# In[26]:


n=int(input())
temp=[]
temp=temp.append(n)


# In[27]:


num=int(input())
count=0
for i in range(1,num):
    while num%i==0:
        count+=1
        i+=1
if count>2:
    print("composite")
else:
    print("NOT COMPOSITE")


# In[28]:


num=int(input())
count=0
i=1
while num%i==0:
    count+=1
    i+=1
if count>2:
    print("composite")
else:
    print("NOT COMPOSITE")


# In[29]:


st="jjbjb"
print(st[:])


# In[30]:


num=int(input())
count=0
i=1
while i<=num:
    if(num%i==0):
        count+=1
    i+=1
#     else:
#         i+=1
if count==2:
    print("prime")
else:
    print("NOT PRIME")


# In[ ]:





# In[31]:


n=5
for i in range(n):
    for j in range(n):
        if i==n-1 or j==n-1 or i+j==n-1 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


# In[32]:


a=[1,2,3,4,5]
key=int(input())
low=a[0]
high=a[len(a)-1]
while high >= low:
    mid = (high+low)//2
    if(a[mid] == key):
        print("Found at " , mid)
        break
    elif(key > a[mid]):
        low = mid + 1
    elif(key < a[mid]):
        high = mid - 1;


# In[33]:


A=[1,3,4,6,7,8]
key = int(input())

found = 0
position = 0

for i in range(len(A)):
    if(A[i] == key):
        found = 1
        position = i
        break

if(found):
    print("Found at", position)
else: 
    print("Not found")


# In[34]:


and arr[low] <= key <= arr[high]
   


# In[ ]:


def interpolation_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high and arr[low] <= key <= arr[high]:
        mid = low + ((key - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Element not found
interpolation_search([1,2,3,6,8,9,12,43,55,63],44)


# In[ ]:


def hash_search(arr, key):
    hash_table = {value: index for index, value in enumerate(arr)}
    return hash_table.get(key,'notfound')  
hash_search([1,33,63,121,12,42,53],120)


# In[ ]:


size=int(input())
arr=[]
for i in range(size):
    elm=int(input())
    arr.append(elm)
arr


# 

# In[ ]:


size=int(input())
arr=[]
for i in range(size):
    elem=int(input())
    arr.append(elem)
num=int(input("tagert value"))
low=0
high=len(arr)-1
while(low<=high):
    mid=(low+high)//2
    if(arr[mid]==num):
        print(1)
        break
    elif(num<arr[mid]):
        high=mid-1
    elif(num>arr[mid]):
        low=mid+1
    else:
        print(-1)


# In[ ]:


def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == key:
            return 1
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


# Example usage
size = int(input("Enter the size of the array: "))
arr = []

print("Enter the elements in sorted order:")
for _ in range(size):
    elem = int(input())
    arr.append(elem)

key = int(input("Enter the key to search: "))

result = binary_search(arr, key)

if result == 1:
    print("Key found!")
else:
    print("Key not found!")


# In[ ]:


#s=int(input())

arr=[]
elems = input().split()
for elem in elems:
    arr.append(int(elem))
arr


# In[ ]:


arr=[]
num=input().split()
key=int(input())
for nums in num:
    arr.append(int(nums))
i=0
while(i>=0):
    if arr[i]==key:
        print("Found")
        break
    i=i+1
else:
    print("not found")
        
 


# In[ ]:


# PYTHON OOP#instances variable
class employee:
    pass
emp_1=employee()
emp_2=employee()
print(emp_1)
print(emp_2)
emp_1.first='pavan'
emp_1.second='sai'
emp_1.email='pavankumar14182@gmail.com'

emp_1.pay=10000000

emp_2.first='subbu'
emp_2.second='penujuli'
emp_2.email='penujulisunnu@gmail.com'
emp_2.pay=10000000000
print(emp_1.first)
print(emp_2.first)


# In[ ]:


class employee:
    def __init__(self,first,last,age,salary):
        self.first=first
        self.last=last
        self.age=age
        
        self.salary=salary
    def full_name(self):
        return '{} {}'.format(self.first,self.last)
emp_1=employee('pavan','sai',20,3000)
emp_2=employee('subbu','sai',20,3000)
print(emp_1.first)
print(emp_2.first)   
print(emp_1.full_name)
print(emp_2.full_name())
print(emp_1.full_name())# printing the instances by using methods
print(employee.full_name(emp_1))#another way of printing instances by using  class name


# In[ ]:


class employee:
    def __init__(self,first,last,age,salary):
        self.first=first
        self.last=last
        self.age=age
        
        self.salary=salary
        
    def full_name():
        return '{} {}'.format(self.first,self.last)
emp_1=employee('pavan','sai',20,3000)
emp_2=employee('subbu','sai',20,3000)
print(emp_1.first)
print(emp_2.first)   
print(emp_1.full_name)
print(emp_2.full_name())
print(emp_1.full_name())# printing the instances by using methods
print(employee.full_name(emp_1))#another way of printing instances by using  class name


# In[ ]:


class employee:
    def __init__(self,first,last,age,salary):
        self.first=first
        self.last=last
        self.age=age
        
        self.salary=salary
        
    def full_name(self):
        return '{} {}'.format(self.first,self.last)
    def appl_pay(self):
        self.salary=int(self.salary*1.04)
emp_1=employee('pavan','sai',20,3000)
emp_2=employee('subbu','sai',20,3000)
print(emp_1.salary)
emp_1.appl_pay()
print(emp_1.salary)


# In[ ]:


arr=["1",3,"hello","write"]
arr[0]=" "
arr[1]=" "
for i in range(0len(arr)+1):
    arr[2]=arr[i]


# In[ ]:


lst=["1","2","4","5","6"]

for i in lst:
#     var=lst.reverse
    print()
    


# In[ ]:


var


# In[ ]:


lst=["1","2","4","5","6"]
temp=[]
size=len(lst)
for i in range (size+1,0):
    temp.append(lst[i])
print(temp)


# In[ ]:


lst


# In[ ]:


for i in range(6):
    for j in range(6):
        print('*'*j)


# In[ ]:


size=int(input())
for i in range(size):
    print('* '*i)

for j in range(size,0,-1):
    print('* '*j)


# In[ ]:


arr=[-1,-2,-3,-4,-5,-6,-7,-8,-9,0,9,8,7,6,5,4,3,2,1]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            pass
arr
        


# In[ ]:


arr=[-1,-2,-3,-4,-5,-6,7,8,-9,0,9,8,7,6,5,4,3,2,1]
count=0
lst=[]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            lst.append(arr[i])
            count+=1
            
        else:
            pass
arr
print(count)
print(lst)
        
    


# In[ ]:


# arr=[-1,-2,-3,-4,-5,-6,7,8,-9,0,9,8,7,6,5,4,3,2,1]
arr=input()
firs=" "
second=" "
arr2=[]
arr2.append(firs)
arr2.append(second)
for i in range(len(arr)):
#     var=firs+second+arr[i]
    arr2.append(arr[i])
arr2   


# In[1]:


get_ipython().system('pip install matlab')
get_ipython().system('pip install matlablib')
from matplotlib import pyplot as plt


# In[2]:


get_ipython().system('pip install --upgrade pip')


# In[3]:


get_ipython().system('pip install python.exe -m pip install --upgrade pip')


# In[8]:



not_exp_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]
not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]
exp_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]
exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
plt.plot(not_exp_x,not_exp_y)
plt.plot(exp_x,exp_y)
plt.xlabel('age')
plt.ylabel('salary')
plt.title('median salary by age')
plt.show()


# In[5]:


from matplotlib import pyplot as plt
ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]
not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]
# exp_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]
exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
plt.plot(ages_x,not_exp_y)# here we created a  single variable that can be used in both graphs 
plt.plot(ages_x,exp_y)
plt.xlabel('age')
plt.ylabel('salary')
plt.title('median salary by age')
plt.show()


# In[6]:


# here we don't know what plot is wht to notice them we uses legeds

from matplotlib import pyplot as plt
ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]
not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]
# exp_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]
exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
plt.plot(ages_x,not_exp_y)# here we created a  single variable that can be used in both graphs 
plt.plot(ages_x,exp_y)
plt.xlabel('age')
plt.ylabel('salary')
plt.title('median salary by age')

plt.legend(["not_expirenced","experinced"])
plt.show()


# In[7]:


# another way to to print legends to plot "BY USING 'label' WE CAN PASS LABELS IN PLT.PLOT"
# here we don't know what plot is wht to notice them we uses legeds

from matplotlib import pyplot as plt
ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]
not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]
# exp_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]
plt.plot(ages_x,not_exp_y,label='not_exp_programming')# by using label
exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,label='exp_programming')
plt.xlabel('age')
plt.ylabel('salary')
plt.title('median salary by age')

# plt.legend(["not_expirenced","experinced"])
plt.show()


#note:- here i have commented the legends so it does displays the legends


# In[8]:


# another way to to print legends to plot "BY USING 'label' WE CAN PASS LABELS IN PLT.PLOT"
# here we don't know what plot is wht to notice them we uses legeds
#NOTE:- HERE IN LEGEND I DON'T PASSES ANY PAREMETERS OR STATEMENT OR TEXTS THE LEGEND WILL AUTO CHECKS THE LABELS 
# AND IT WILL DIPLAY THE MSG THAT PRESENT IN THE LABEL
from matplotlib import pyplot as plt
ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]
not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]
# exp_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]
plt.plot(ages_x,not_exp_y,label='not_exp_programming')# by using label
exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,label='exp_programming')
plt.xlabel('age')
plt.ylabel('salary')
plt.title('median salary by age')

plt.legend()
plt.show()


# In[9]:


# FORMATTING THE PLOT{IN THESE I CAN GIVE COLOUR TO THE PLOT AND I CAN GIVE STYLE TO THE PLOT }
# '[MARKER][LINE][COLOR]'  ---->SYNTAX

from matplotlib import pyplot as plt

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,'k--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,'b',label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.show()


# In[10]:


# FORMATTING THE PLOT{IN THESE I CAN GIVE COLOUR TO THE PLOT AND I CAN GIVE STYLE TO THE PLOT }
# '[MARKER][LINE][COLOR]'  ---->SYNTAX
#  i have tryed to give formatting string in these way [MARKER][COLOR] that means we can write in anyway for formattingt plotting
#just observe above code's formatting or marker sytle
from matplotlib import pyplot as plt

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,'--k',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,'-b',label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.show()


# In[9]:


# FORMATTING THE PLOT{IN THESE I CAN GIVE COLOUR TO THE PLOT AND I CAN GIVE STYLE TO THE PLOT }
# '[MARKER][LINE][COLOR]'  ---->SYNTAX
# to make our read we use these way
from matplotlib import pyplot as plt

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='k',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='b',linestyle='-',label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.show()


# In[10]:


# FORMATTING THE PLOT{IN THESE I CAN GIVE COLOUR TO THE PLOT AND I CAN GIVE STYLE TO THE PLOT }
# '[MARKER][LINE][COLOR]'  ---->SYNTAX
# ADDED MAKER STYLE

from matplotlib import pyplot as plt

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='k',linestyle='--',marker='.',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='b',linestyle='-',marker='o' ,label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.show()


# In[11]:


# FORMATTING THE PLOT{IN THESE I CAN GIVE COLOUR TO THE PLOT AND I CAN GIVE STYLE TO THE PLOT }
# '[MARKER][LINE][COLOR]'  ---->SYNTAX
# ADDED hex value these meams that we are giving a value to color ex-#444444(grey colour),like these we will have hex_values to every color
# hex value should be in single code like these '#44444' not like these #444444
from matplotlib import pyplot as plt

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',marker='.',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',marker='o',label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.show()


# In[12]:


# FORMATTING THE PLOT{IN THESE I CAN GIVE COLOUR TO THE PLOT AND I CAN GIVE STYLE TO THE PLOT }
# '[MARKER][LINE][COLOR]'  ---->SYNTAX
# ADDED hex value these meams that we are giving a value to color ex-#444444(grey colour),like these we will have hex_values to every color
# hex value should be in single code like these '#44444' not like these #444444
from matplotlib import pyplot as plt

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.show()


# In[13]:


# here i neeed experinced line to thicker so i can use linewidth in the formatter 
from matplotlib import pyplot as plt

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.show()


# In[14]:


# padding
from matplotlib import pyplot as plt

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.show()


# In[15]:


#adding grid by using these we can say when the not_exp_programming increased or decreased
# in simple term their are use to visual the data
# padding
from matplotlib import pyplot as plt

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.grid(True)  # grid declaration

plt.show()


# In[ ]:





from matplotlib import pyplot as plt

print(plt.style.available)# by these plt.style.available i can get the all the style that are in matlablib

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.grid(True)  # grid declaration

plt.show()


# In[ ]:


# by using Solarize_Light2 we plotted graph


from matplotlib import pyplot as plt

plt.style.use("Solarize_Light2")

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.grid(True)  # grid declaration

plt.show()


# In[ ]:


# by using _classic_test_patch  we plotted graph


from matplotlib import pyplot as plt

plt.style.use('_classic_test_patch')

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.grid(True)  # grid declaration

plt.show()


# In[ ]:


# by using '_mpl-gallery' we plotted graph


from matplotlib import pyplot as plt

plt.style.use('_mpl-gallery')

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.grid(True)  # grid declaration

plt.show()


# In[ ]:


# by using 'bmh' we plotted graph


from matplotlib import pyplot as plt

plt.style.use('bmh')

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.grid(True)  # grid declaration

plt.show()


# In[ ]:


# by using '_mpl-gallery-nogrid' we plotted graph


from matplotlib import pyplot as plt

plt.style.use('_mpl-gallery-nogrid')

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.grid(True)  # grid declaration

plt.show()


# In[ ]:


# by using 'classic' we plotted graph


from matplotlib import pyplot as plt

plt.style.use('classic')

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.grid(True)  # grid declaration

plt.show()


# In[ ]:


# by using 'dark_background' we plotted graph


from matplotlib import pyplot as plt

plt.style.use('dark_background')

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.grid(True)  # grid declaration

plt.show()


# In[ ]:


# by using 'fast' we plotted graph


from matplotlib import pyplot as plt

plt.style.use('fast')

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.grid(True)  # grid declaration

plt.show()


# In[ ]:


# by using 'fivethirtyeight' we plotted graph

#  'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10'
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.grid(True)  # grid declaration

plt.show()


# In[ ]:


# by using ''ggplot' we plotted graph


from matplotlib import pyplot as plt

plt.style.use('ggplot')

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.grid(True)  # grid declaration

plt.show()


# In[ ]:


# by using 'grayscale' we plotted graph

# 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10'
from matplotlib import pyplot as plt

plt.style.use('grayscale')

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.grid(True)  # grid declaration

plt.show()


# In[ ]:


# by using 'seaborn', we plotted graph

#  'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10'
from matplotlib import pyplot as plt

plt.style.use('seaborn')



ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.grid(True)  # grid declaration

plt.show()


# In[ ]:


# by using 'seaborn-bright', we plotted graph

#   'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10'
from matplotlib import pyplot as plt

plt.style.use('seaborn-bright',)

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.grid(True)  # grid declaration

plt.show()


# In[ ]:


# by using 'seaborn-colorblind' we plotted graph

#   'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10'
from matplotlib import pyplot as plt

plt.style.use('seaborn-colorblind')

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.grid(True)  # grid declaration

plt.show()


# In[ ]:


# by using ''seaborn-dark'' we plotted graph

#   'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10'
from matplotlib import pyplot as plt

plt.style.use('seaborn-dark')

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.grid(True)  # grid declaration

plt.show()


# In[ ]:


# by using 'seaborn-dark-palette' we plotted graph

#   'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10'
from matplotlib import pyplot as plt

plt.style.use('seaborn-dark-palette')

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.grid(True)  # grid declaration

plt.show()


# In[ ]:


# by using seaborn-darkgrid' we plotted graph

#    'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10'
from matplotlib import pyplot as plt

plt.style.use('seaborn-darkgrid')

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.grid(True)  # grid declaration

plt.show()


# In[ ]:


# by using 'tableau-colorblind10' we plotted graph

#  'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10'
from matplotlib import pyplot as plt

plt.style.use('tableau-colorblind10')

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.grid(True)  # grid declaration

plt.show()


# In[ ]:


# by using 'seaborn-muted' we plotted graph

#  'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10'
from matplotlib import pyplot as plt

plt.style.use('seaborn-muted')

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.grid(True)  # grid declaration

plt.show()


# In[ ]:


# by using 'seaborn-notebook' we plotted graph

#    'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10'
from matplotlib import pyplot as plt

plt.style.use('seaborn-notebook')

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.grid(True)  # grid declaration

plt.show()


# In[ ]:


# by using 'seaborn-paper' we plotted graph

#  'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10'
from matplotlib import pyplot as plt

plt.style.use('seaborn-paper')

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.grid(True)  # grid declaration

plt.show()


# In[ ]:


# by using ''seaborn-pastel'' we plotted graph

#  'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10'
from matplotlib import pyplot as plt

plt.style.use('seaborn-pastel')

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.grid(True)  # grid declaration

plt.show()


# In[ ]:


# by using 'seaborn-poster' we plotted graph

#'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10'
from matplotlib import pyplot as plt

plt.style.use('seaborn-poster')

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.grid(True)  # grid declaration

plt.show()


# In[ ]:


# by using 'seaborn-talk'' we plotted graph

# 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10'
from matplotlib import pyplot as plt

plt.style.use('seaborn-talk')

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.grid(True)  # grid declaration

plt.show()


# In[ ]:


# by using 'seaborn-ticks'' we plotted graph

#  'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10'
from matplotlib import pyplot as plt

plt.style.use( 'seaborn-ticks')

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.grid(True)  # grid declaration

plt.show()


# In[ ]:


# by using 'seaborn-white' we plotted graph

# 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10'
from matplotlib import pyplot as plt

plt.style.use('seaborn-white')

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.grid(True)  # grid declaration

plt.show()


# In[ ]:


# by using  'seaborn-whitegrid'' we plotted graph

#   'seaborn-whitegrid', 'tableau-colorblind10'
from matplotlib import pyplot as plt

plt.style.use(  'seaborn-whitegrid')

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,color='#5a7d9a',linestyle='--',label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,color='#adad3b',linestyle='-',linewidth="5",label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.grid(True)  # grid declaration

plt.show()


# In[ ]:


# by using 'seaborn-ticks'' we plotted graph

#  'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10'
from matplotlib import pyplot as plt

plt.style.use('seaborn-whitegrid')

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()


plt.show()


# In[ ]:



from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()


plt.show()


# In[ ]:



from matplotlib import pyplot as plt

plt.style.use('ggplot')

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()


plt.show()


# In[ ]:


# matplotlib xkcd comic method
from matplotlib import pyplot as plt

plt.xkcd()

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()


plt.show()


# In[ ]:


# saving the figure in my directory or we can give addrees where we need to save it
# plt,savefig(addrees,plot.png)
from matplotlib import pyplot as plt

plt.xkcd()

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()

plt.savefig('plot.png')

plt.show()


# In[ ]:


# matplotlib xkcd comic method
from matplotlib import pyplot as plt

plt.xkcd()

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.plot(ages_x,not_exp_y,label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
 
plt.plot(ages_x,exp_y,label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()


plt.show()


# In[ ]:


from matplotlib import pyplot as plt


# In[ ]:


# matplotlib xkcd comic method
from matplotlib import pyplot as plt

# plt.xkcd()

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.bar(ages_x,not_exp_y,label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

# exp_y=[45435,48856,45662,45565,55535,54636,56635,
#        53535,65454,68541,78956,81562,91165]
 
# plt.plot(ages_x,exp_y,label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

# plt.tight_layout()


plt.show()


# In[39]:


# matplotlib xkcd comic method
from matplotlib import pyplot as plt

# plt.xkcd()

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]

plt.bar(ages_x,not_exp_y,label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

# exp_y=[45435,48856,45662,45565,55535,54636,56635,
#        53535,65454,68541,78956,81562,91165]
 
# plt.bar(ages_x,exp_y,label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

plt.tight_layout()


plt.show()


# In[57]:


# at here the 2 plots are arrage in same bar 
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

not_exp_y=[2000034, 2134000, 2203500, 2302400, 2400042, 2245000,
   2602100, 2700560, 2128000, 2900120, 1230000, 310020,3204200]

plt.bar(ages_x,not_exp_y,label='not_exp_programming')# note :- we should only use the lowe case letter for colouring here k-black,and i have given the maker style to the line that is dash line(--)

exp_y=[42315,41836,42462,45265,5334435,544536,56635,
       53525,6554,6348541,7893,81322,9145]
 
plt.bar(ages_x,exp_y,label='exp_programming')# note :- we should only use the lowe case letter for colouring here b-blue,and here i have not given any marker style by default the  python will consider the solid line as maker style

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

# plt.tight_layout()


plt.show()


# In[65]:


# at here the 2 plots are arrage in same bar now i wiil do the separation of two bar by importing numpys
import numpy as np


from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]

x_indexes=np.arange(len(ages_x))#THESE IS USEFUL FOR THE GIVING RANGE TO MY DATA 

width=0.25# SEE HERE I GIVE WIDTH THAT IS USEFUL FOR THE SEPARATUON OF TWO DATA 

not_exp_y=[2000034, 2134000, 2203500, 2302400, 2400042, 2245000,
   2602100, 2700560, 2128000, 2900120, 1230000, 310020,3204200]

# plt.bar(x_indexes-width,not_exp_y,width=width,label='not_exp_programming')
plt.bar(x_indexes,not_exp_y,width=width,label='not_exp_programming')

exp_y=[42315,41836,42462,45265,5334435,544536,56635,
       53525,6554,6348541,7893,81322,9145]
 
plt.bar(x_indexes-width,exp_y,width=width,label='exp_programming')

plt.xlabel('age')

plt.ylabel('salary')

plt.title('median salary by age')

plt.legend()

# plt.tight_layout()


plt.show()


# In[ ]:


import numpy as np


from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

ds=


# In[1]:


lst=[10,3,15,22,17]
print(min(lst))


# In[26]:


def bin(arr,l,h,key):
    while l<=h:
        mid =(l+h)//2
        if arr[mid]==key:
            return mid
        elif  arr[mid]>key:
            h=mid-1
        else:
            l=mid+1
    return -1

arr=[1,4,23,42,55,64,65]
n=len(arr)
key=int(input())
result=bin(arr,0,n-1,key)
if result==-1:
    print("element not found")
else:
    print("element is found at index: ",result)


# In[25]:


def bin(arr,l,h,key):
    while l<=h:
        mid =(l+h)//2
        if arr[mid]==key:
            return mid
        elif  arr[mid]==key:
            h=mid-1
        else:
            l=mid+1
    return -1
if __name__=="__main__":
    
    arr=[1,4,23,42,55,64,65]
    n=len(arr)
    key=int(input())
    result=bin(arr,0,n-1,key)
    if result==-1:
        print("element not found")
    else:
        print("element is found at index: ",result)


# In[32]:


a=[1,4,23,42,55,64,65]
key=int(input())
low=a[0]
high=a[-1]

while( high >= low):
    mid = (high+low)//2
    if(a[mid] == key):
        print("Found at " , mid)
        break
    elif(key > a[mid]):
        low = mid + 1
    elif(key < a[mid]):
        high = mid - 1;


# In[35]:


lst=[10,3,15,22,17]

for i in range(len(lst)):#01
    for j in range(i+1):#01
        if lst[i]<lst[j]:
            lst[i],lst[j]=lst[j],lst[i]
    
        else:
              pass
lst


# In[37]:


lst = [10, 3, 15, 22, 17]

for i in range(len(lst)):#0
    for j in range(i):#
        if lst[i] < lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

lst


# In[5]:


# here we don't know what plot is wht to notice them we uses legeds

from matplotlib import pyplot as plt
ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]
not_exp_y=[20000, 21000, 22000, 23000, 24000, 25000,
   26000, 27000, 28000, 29000, 30000, 31000,32000]
# exp_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]
exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
plt.plot(ages_x,not_exp_y,label='no experinced',marker='.')# here we created a  single variable that can be used in both graphs 
plt.plot(ages_x,exp_y,label='expe',marker='.')
plt.xlabel('age')
plt.ylabel('salary')
plt.title('median salary by age')

plt.legend()
plt.show()


# In[12]:


ages_x=[18,19,20,21,22,23,24,25,26,27,28,29,30]
exp_y=[45435,48856,45662,45565,55535,54636,56635,
       53535,65454,68541,78956,81562,91165]
plt.style.use('scatter_plot')
plt.plot(ages_x,exp_y,marker='.')
plt.xlabel('age')
plt.ylabel('exp_y')
plt.title('median salary by age')
plt.show()


# In[ ]:




