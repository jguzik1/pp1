n_product = input("Add new product: ")

file = open('shopping.txt', 'a', encoding='UTF-8')

file.write(n_product)
file.write("\n")

file.close()