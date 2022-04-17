import csv
from prodykt import Prodykt
class Magazin:
    name = []
    prise = []
    stat = []
    id_ = []
    def __init__(self):
        with open('magazin.csv',encoding='UTF-8') as csv_file:
            csv_readen=csv.reader(csv_file, delimiter=';')
            for row in csv_readen:
                self.name.append(row[0])
                self.prise.append(int(row[1]))
                self.stat.append(int(row[2]))
                self.id_.append(int(row[3]))
    def __str__(self):
        s=''
        for i in range(len(self.name)):
            s+=str(self.duy(i))+'\n'
        return s
    def duy(self, i):
            return Prodykt(self.name[i], self.prise[i], self.stat[i], self.id_[i])








