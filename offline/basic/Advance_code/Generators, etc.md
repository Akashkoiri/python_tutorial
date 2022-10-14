#

## All new terms in python

### What is an iterable?

```py
# Iterable is nothing but a collection of elements which can be iterate
lst = [1,2,3,4,5]
tup = (1,2,3,4,5)
```

### What is an iterator?

```py
# Iterator is nothing but a collection of elements which can be iterate only once
itr = iter([1,2,3,4,5])

# Call an element of an iterator
print(next(itr))
print(next(itr))

# When we use next() function, then the exception not handled after completing the iteration, but when we use a for loop to iterate then exception will handled automaticly
for i in iterator:
    print(i)

# As we iterate through an iterator the values will disappeared one by one
for i in itr:
    print(i)
    print('End')
    break

for i in itr:
    print(i)
```
