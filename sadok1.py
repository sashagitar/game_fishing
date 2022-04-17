from fishing import Fishing
from sadok import Sadok
f = Fishing()
s = Sadok()
for i in range(10):
    g = f.go_fishing()
    if g != None:
        s.add(g)
print(s)