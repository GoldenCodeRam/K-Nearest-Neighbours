import sys
sys.path.append("..")
from models.Bovine import bovine
import csv

class readFile():
    
    def __init__(self, nameFile):
        self.nameFile = nameFile

    def getListBovines(self):
        bovines = []
        with open(self.nameFile) as f:
            reader = csv.reader(f)
            for row in reader:
                bovineC = bovine(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])
                bovines.append(bovineC)
        return bovines


    