'''Task 2
Реалізуйте простий перекладач, який використовує словник для збереження пар слів. Користувач може вводити слово, а /
програма повертає його переклад. У цьому випадку, словник може використовуватись для збереження відповідностей між /
словами у різних мовах.
Приклад:
translations = {
    'hello': 'привіт',
    'goodbye': 'до побачення',
    'cat': 'кіт',
    'dog': 'собака'
}'''
slovo = input('введи слово для перевода - ')
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
    'мяч': 'ball'
     }
if ord(slovo[0]) > 122:
    res = translations.get(slovo.lower())
    print(f'перевод - {res} ')
if ord(slovo[0]) <= 122:
    for key, value in translations.items():
        if value == slovo.lower():
            print(f'перевод - {key}')
