from fish import Fish
from fishing import Fishing
from holodos import Holodos
from magaz import Magazin
from pers import Pers
from prodykt import Prodykt
from sadok import Sadok
f = Fishing()
s = Sadok()
for i in range(5):
    fish = f.go_fishing()
    if fish != None:
        s.Add(fish)

print(s)