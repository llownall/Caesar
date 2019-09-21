import sys
import os

if sys.argv[1] == '-help':
    print('аргумент1 - имя файла с зашифрованным текстом\n'
          'аргумент2 - output\n'
          'далее ОПЦИОНАЛЬНО!\n'
          '-k аргумент3 - имя файла с ключом\n')
    exit()


class color:
    Red = '\033[41m'
    End = '\033[0m'


def by_key(key, colored=True):
    text = list(open(sys.argv[1], encoding='utf-8').read())
    result = list()
    red = color.Red if colored else ''
    end = color.End if colored else ''
    for char in text:
        result.append(chr(key.index(char) + ord('а')) if key.count(char) > 0 else (red + char.upper() + end))

    return result


def bruteforce(key):
    result = by_key(key)
    while key.count('?') > 0:
        os.system('cls')
        print('Напишите "end", если хотите закончить')

        alphabet = list()
        for i in range(ord('а'), ord('я') + 1):
            alphabet.append(chr(i))
        print(*alphabet, sep='')
        print(*key, sep='')
        print(*result, sep='')

        what = input('Что заменить? ')
        if what == 'end':
            break
        to = input('На что? ')
        key[ord(to) - ord('а')] = what
        result = by_key(key)

        out = open('key_' + sys.argv[2], 'w', encoding='utf-8')
        out.write(''.join(key))
        out.close()

    result = by_key(key, False)
    out = open(sys.argv[2], 'w', encoding='utf-8')
    out.write(''.join(result))

    print(f'saved to {sys.argv[2]}')
    print(f'key saved to key_{sys.argv[2]}')


def comparator():
    text = open(sys.argv[1], encoding='utf-8').read()

    info = input('Введите "Фамилия Имя" членов бригады\n').lower().replace(' ', '')
    text_ = text[-len(info):]

    key = list()
    for i in range(32):
        key.append('?')
    for i in range(len(text_)):
        key[ord(info[i]) - ord('а')] = text_[i]

    return key


if len(sys.argv) != 3 and len(sys.argv) != 5:
    raise Exception('wrong args')
elif len(sys.argv) == 5:
    if sys.argv[3] == '-k':
        bruteforce(list(open(sys.argv[4], encoding='utf-8').read()))
else:
    bruteforce(comparator())
