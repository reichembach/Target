str = input('String: ')
novostr = ''
index = len(str)-1
while index >= 0:
    novostr = novostr + str[index]
    index = index - 1
print('String invertida:', novostr)
