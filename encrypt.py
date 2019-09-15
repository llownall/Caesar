import sys

if sys.argv[1] == '-help':
    print('аргумент1 - имя файла с ключём\n'
          'аргумент2 - имя файла с текстом\n'
          'аргумент3 - output\n')
    exit()

if len(sys.argv) != 4:
    raise Exception('wrong args')

key = list(open(sys.argv[1], encoding='utf-8').read())

text = list(open(sys.argv[2], encoding='utf-8').read().lower())
text = [char for char in text if char in key]

result = list()
for char in text:
    result.append(key[(ord(char) - ord('а'))])

out = open(sys.argv[3], 'w', encoding='utf-8')
out.write(''.join(result))
print(f'saved to {sys.argv[3]}')
