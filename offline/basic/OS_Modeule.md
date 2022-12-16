# OS Modeule Tutorial
---
### How to import os modelue?
```py
import os
```

### How to run windows commands?
```py
os.system('dir')
```

### How to get current working directory?
```py
os.getcwd()
```

### How to change current working directory?
```py
os.chdir("C://")
```

### How to see all the items in the current working directory?
```py
os.listdir()
```

### How to make a directory?
```py
os.mkdir('test')
os.mkdir('test/inner_test')
```

### How to make multiple directories?
```py
os.makedirs('outer/inner')
# We can also create single directories using makedirs
os.makedirs('test2')
```

### How to rename a file?
```py
os.rename('file.txt', 'test_file.txt')

# Ex:
file_name = os.path.join('C://', 'test.txt')
os.rename(file_name, 'changed.txt')
```

### How to see environment variables?
```py
os.environ.items()
os.environ.get('PATH')
```

### How to join two paths very securely?
```py
os.path.join('C://', '/file.txt')
```

### How to check a path is exist or not?
```py
os.path.exists('C://folder')
```

