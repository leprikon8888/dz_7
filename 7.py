'''Task 3
Напишіть програму, яка приймає словник і перевіряє, чи містяться в ньому унікальні значення.'''

translations = {
    'кот': 'cat',
    'дом': 'house',
    'машина': 'car',
    'солнце': 'sun',
    'дерево': 'tree',
    'вода': 'water',
    'книга': 'book',
    'цветок': 'flower',
    'школа': 'school',
    'мяч': 'ball',
    'кот2': 'cat',
    'кот3': 'cat',
    'кот4': 'cat'
     }
my_set = set()
for item in translations.values():
    if item not in my_set:
        my_set.add(item)
if len(my_set) > 1:
    print('словарь содержит уникальные значения')
else:
    print('словарь не содержит уникальные значения')