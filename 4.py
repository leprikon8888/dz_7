'''Task 4
Напишіть програму, яка конвертуватиме суму з однієї валюти в іншу, використовуючи словник з курсами обміну.'''

kurs_prodaja = {
    'доллар': 38.00,
    'евро': 40.35
}

kurs_pokupka = {
    'доллар': 37.90,
    'евро': 40.2
}
operation = (input('вы бы хотели купить или продать валюту: введи купить или продать - ')).lower()
if operation != 'купить' and operation != 'продать':
    print('такая операции недоступна')


if operation.lower() == 'купить':
    summa = float(input('введите сумму в гривне, которая у вас есть: '))
    val = (input('доллар или евро? - ')).lower()
    if val == 'доллар':
        res = summa // kurs_prodaja['доллар']
        sda4a = summa % kurs_prodaja['доллар']
        print(f'вы сможете купить у нас - {res} долларов, сдача составит {sda4a} грн')


    elif val == 'евро':
        res = summa // kurs_prodaja['евро']
        sda4a = summa % kurs_prodaja['евро']
        print(f'вы сможете купить у нас - {res} евро, сдача составит {sda4a:.2f} грн')

if operation.lower() == 'продать':
    val = (input('доллар или евро? - ')).lower()
    summa = float(input('введите сумму в валюте, которая у вас есть: '))
    if val == 'доллар':
        res = summa * kurs_pokupka['доллар']
        print(f'вы получите - {res:.2F} грн')
    elif val == 'евро':
        res = summa * kurs_pokupka['евро']
        print(f'вы получите - {res:.2F} грн')