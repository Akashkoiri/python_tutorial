#

## Advanced python syntax

### range(len(data)) ==> enumerate(data)

```py
data = [1,2,-4,-5]
for i,val in enumerate(data):
    if val < 0:
        data[i] = 0
print(data)
```

### How to use map()

```py
# map() is used when we want to apply a function to all of the value of a list,tuple in one line
nums = ['1','2','3','4','5']
nums = list(map(int, nums))
print(nums)

# Also we can use lambda in the map()
nums = [1,2,3,4,5]
squares = list(map(lambda x: x*x, nums))
print(squares)

# How can we apply two functions on a list at the same time
nums = [1,2,3,4,5]

def square(x):
    return x*x
def cube(x):
    return x**3
name = [square,cube]

for i in nums:
    val = list(map(lambda x: x(i), name))
    print(val)
```

### How to use filter()

```py
# filter those values from a list which are giving us true when we pass them in a function
nums = [1,2,3,4,5,6,7,8,9]

def is_greater(x):
    return x>5

list1 = list(filter(is_greater,nums))
print(list1)
```

### How to loop through multiple lists at a time

```py
list1 = [1,2,3,4]
list2 = ['akash','sagar','sujal','chandu','bikash']
list3 = [5,6,7,8]

for val1,val2,val3 in zip(list1,list2,list3):
    print(val1,val2,val3)
```

### No need to type any sorting algorithms

```py
# using python inbuilt function (list,tuple,dictionary)
data = [1,4,7,3,5,2,8,6]
data = sorted(data, reverse=True)
print(data)

# sorte a dictionary in a list
data = [
    {'name':'akash','age':18},
    {'name':'sujal','age':17},
    {'name':'chandu','age':20}
]
data = sorted(data,key=lambda x: x['age'])
print(data)
```

### How to count values of a list

```py
from collections import Counter

data = [10,10,3,10,4,5,3,7,10,3,4]
print(Counter(data))
print(Counter(data)[4])
```

### concat strings using join function

```py
strings = ['hello','world!']
string = "_".join(strings)
print(string)
```

### merge two dictionaries

```py
d1 = {'name':'akash','age':20}
d2 = {'naam':'akash','stream':'arts'}
d3 = {**d1, **d2}
print(d3)
```
