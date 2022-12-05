MaF = open("07-FileHandling\MeatAndFish.txt","r")
BaG = open("07-FileHandling\GrainsAndBread.txt","r")
shlist = open("07-FileHandling\shoppinglist.txt", "w")

sum_of_zakupys = MaF.read() + BaG.read()
MaF.close()
BaG.close()

shlist.write(sum_of_zakupys)

shlist.close()