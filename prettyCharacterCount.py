import pprint
message = 'If you import the pprint module into your programs, you’ll have access to the pprint() and p format() functions that will “pretty print” a dictionary’s values. This is helpful when you want a cleaner display of the items in a dictionary than what print() provides '

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
    
#pprint.pprint(count)

print(pprint.pformat(count))