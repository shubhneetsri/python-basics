from collections import namedtuple

res = namedtuple('Employee', ['Name', 'Age'])

e1 = res('test', 12)

print(e1)