def ile_razy(check, text):
    count = 0
    for letter in text:
        if letter == check:
            count += 1
    return count

przyklad = 'You never get a second chance to make a first impression'
szukana = 'e'

print(ile_razy(szukana,przyklad))