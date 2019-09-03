import sys

magic_const = 1072


def by_key(key=None):
    if key is None:
        key = list(open(sys.argv[3], encoding='utf-8').read())

    text = list(open(sys.argv[1], encoding='utf-8').read())
    result = list()
    for char in text:
        result.append(chr(key.index(char) + magic_const) if key.count(char) > 0 else '?')
    print(*result, sep='')

    out = open('decrypted.txt', 'w', encoding='utf-8')
    out.write(''.join(result))
    print(f'saved to decrypted.txt')


def crack():
    text = open(sys.argv[1], encoding='utf-8').read()

    info = input('Введите "Фамилия Имя" членов бригады\n').lower().replace(' ', '')
    text_ = text[-len(info):]

    key = list()
    for i in range(33):
        key.append(' ')
    for i in range(len(text_)):
        key[ord(info[i]) - magic_const] = text_[i]
    by_key(''.join(key))


if len(sys.argv) != 2 and len(sys.argv) != 4:
    raise Exception('wrong args')
elif len(sys.argv) == 4:
    if sys.argv[2] == '-k':
        by_key()
else:
    crack()
