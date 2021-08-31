import readCsv

testRead = readCsv.readFile("NeosporaHoja1.csv")

listBovines = testRead.getListBovines()

for obj in listBovines:
    print(obj.toString()) 