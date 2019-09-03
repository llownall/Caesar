import sys

magic_const = 1072

if len(sys.argv) != 4:
    raise Exception('wrong args')

key = list(open(sys.argv[1], encoding='utf-8').read())

text = list(open(sys.argv[2], encoding='utf-8').read().lower())
text = [char for char in text if char in key]

result = list()
for char in text:
    # print(f'{char} index is {ord(char) - magic_const} new char {key[(ord(char) - magic_const)]}')
    result.append(key[(ord(char) - magic_const)])
print(*result, sep='')

out = open(sys.argv[3], 'w', encoding='utf-8')
out.write(''.join(result))
print(f'saved to {sys.argv[3]}')
