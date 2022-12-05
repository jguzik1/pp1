import re

text = "To be, or not to be, that is the question"

words = re.findall("[A-z]+",text)

print(len(words))