import csv
from prodykt import Prodykt
class Magaz:
    name = []#
    price = []#
    stats = []#
    id_ = []#
    eda = []#

    def __init__(self) -> None:
        with open('magazin.csv', encoding = 'UTF-8') as csv_file:
            csv_reader = csv.reader(csv_file,delimiter = ';')
            for row in csv_reader:
                self.name.append(row[0])
                self.price.append(int(row[1]))
                self.stats.append(int(row[2]))
                self.id_.append(int(row[3]))

    def __str__(self):
        s=''
        for i in range(len(self.name)):
            s += str(self.duy(i))+'\n'
        return s
        
    def duy(self, i):
        if i >= len(self.name):
            return None
        else:
            return Prodykt(self.id_[i],self.name[i], self.price[i], self.stats[i])