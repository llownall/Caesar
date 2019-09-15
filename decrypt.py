import sys

if sys.argv[1] == '-help':
    print('аргумент1 - имя файла с зашифрованным текстом\n'
          'аргумент2 - output\n'
          'далее ОПЦИОНАЛЬНО!\n'
          '-k аргумент3 - имя файла с ключом\n')
    exit()

def by_key(key=None):
    if key is None:
        key = list(open(sys.argv[3], encoding='utf-8').read())

    text = list(open(sys.argv[1], encoding='utf-8').read())
    result = list()
    for char in text:
        result.append(chr(key.index(char) + ord('а')) if key.count(char) > 0 else '?')

    out = open(sys.argv[2], 'w', encoding='utf-8')
    out.write(''.join(result))
    print(f'saved to {sys.argv[2]}')


def crack():
    text = open(sys.argv[1], encoding='utf-8').read()

    info = input('Введите "Фамилия Имя" членов бригады\n').lower().replace(' ', '')
    text_ = text[-len(info):]

    key = list()
    for i in range(33):
        key.append(' ')
    for i in range(len(text_)):
        key[ord(info[i]) - ord('а')] = text_[i]
    by_key(''.join(key))


if len(sys.argv) != 3 and len(sys.argv) != 5:
    raise Exception('wrong args')
elif len(sys.argv) == 5:
    if sys.argv[2] == '-k':
        by_key()
else:
    crack()
