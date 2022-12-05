n_product = input("Add new product: ")

file = open('07-FileHandling\shopping.txt', 'a', encoding='UTF-8')

file.write(n_product)
file.write("\n")

file.close()