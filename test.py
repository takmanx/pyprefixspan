from pyprefixspan import pyprefixspan
from pprint import pprint

data = [
    'a c d',
    'a b c',
    'c b a',
    'a a b'
]
minsup = 2
len = 1

p = pyprefixspan(data)
print(vars(p))
p.setminsup(2)
print(vars(p))

p.setlen(1)
print(vars(p))

p.run()

print(vars(p))

print(p.out)

