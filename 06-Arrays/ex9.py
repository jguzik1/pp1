arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

longest = arr[0]

for imie in arr:
    if len(imie) > len(longest):
        longest = imie

print(longest)