import random
import sys

if sys.argv[1] == '-help':
    print('аргумент1 - output')
    exit()

if len(sys.argv) != 2:
    raise Exception('wrong args')

alphabet = list()
for i in range(ord('а'), ord('я') + 1):
    alphabet.append(chr(i))
print(*alphabet)

for i in range(len(alphabet) - 1, 1, -1):
    j = random.randint(0, i)
    temp = alphabet[j]
    alphabet[j] = alphabet[i]
    alphabet[i] = temp

print(*alphabet)

out = open(sys.argv[1], 'w', encoding='utf-8')
for char in alphabet:
    out.write(char)
print('saved to key.txt')
