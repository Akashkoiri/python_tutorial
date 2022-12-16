
---
### Handling All Exceptions at once

```py
try:
    print(5 + 'a')
except Exception as e:
    print('Wrong statement', e)
```

### Specific Exception Handling

```py
a = 5
b = 0

try:
    print(a/b)
except ZeroDivisionError:
    print("Can't devide with zero")
```