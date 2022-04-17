from fishing import Fishing
from sadok import Sadok
f = Fishing()
g = f.go_fishing()
s = Sadok()
for i in range(4):
    g = f.go_fishing()
    if g != None:
        s.add(g)
print(s)