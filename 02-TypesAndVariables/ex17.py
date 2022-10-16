h_cm = int(input('podaj wzrost w cm: '))

h_in = h_cm / 2.54

h_ft = int(h_in // 12184.5)

h_in = int(h_in % 12)

print(f'wzrost cm: {h_cm}cm \nwzrost ft, in: {h_ft}ft {h_in}in')