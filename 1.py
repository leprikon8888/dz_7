'''Task 1
Напишіть програму, яка приймає рядок тексту і повертає словник, де ключами є слова, а значеннями - кількість входжень/
кожного слова в тексті.'''
txt = 'world Python world  Java Hello Python  world  world Python Java Hello world world  Python Java Hello Java'
a = txt.split()
b = set(a)
res = {}
for item in b:
    res[item] = txt.count(item)
print(res)