fib = 0
fiba = 0
inp = input('Número: ')
while True:
    try:
        iinp = int(inp)
    except:
        print('Input Inválido')
        inp = input('Número: ')
        continue
    if iinp == fib:
        print('Número pertence a sequência de Fibonacci')
        break
    elif iinp < fib:
        print('Número não pertence a sequência de Fibonacci')
        break
    else:
        if fib == 0:
            fib = fib + 1
        else:
            fibi = fiba
            fiba = fib
            fib = fib + fibi
