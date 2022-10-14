lst = [1,2,3,4,5] # called Iterable

# This var is called iterator
itr = iter(lst)

# for i in iterator:
#     print(i)
#     print('End')
#     break

for i in iterator:
    print(i)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
try:
    print(next(itr))
except StopIteration:
    print('Iterator is empty')