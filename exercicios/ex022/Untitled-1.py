while True:
    a = int(input('Minuto: '))
    b = int(input('Número anterior: '))
    c = a + b
    if c == 60:
        c = 0
    elif c > 60:
        c = c - 60

    print(f'Próximo branco cai no minuto {c}')