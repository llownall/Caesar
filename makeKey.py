import random
import sys

if len(sys.argv) != 2:
    raise Exception('wrong args')

alphabet = list(open(sys.argv[1], encoding='utf-8').read())
print(*alphabet)

for i in range(len(alphabet) - 1, 1, -1):
    j = random.randint(0, i)
    temp = alphabet[j]
    alphabet[j] = alphabet[i]
    alphabet[i] = temp

print(*alphabet)

out = open('key.txt', 'w', encoding='utf-8')
for char in alphabet:
    out.write(char)
print('saved to key.txt')
