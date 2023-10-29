from itertools import product
import string

min_len = 1
max_len = 1
counter = 0
character = string.ascii_lowercase+string.digits+string.ascii_uppercase+string.punctuation+string.digits

file_open = open("password-list.txt",'w')

for i in range(min_len,max_len+1):
    for j in product(character,repeat=i):
        word = "".join(j)
        file_open.write(word)
        file_open.write("\n")
        counter+=1
print('Wordlist of {} passwords created'.format(counter))