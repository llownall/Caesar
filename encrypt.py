import sys

if len(sys.argv) != 4:
    raise Exception('wrong args')

key = list(open(sys.argv[1], encoding='utf-8').read())
print(*key)

text = list(open(sys.argv[2], encoding='utf-8').read().lower().replace(' ', ''))
print(*text, sep='')









# out = open(sys.argv[2], 'w', encoding='utf-8')
# print(f'saved to {sys.argv[2]}')
