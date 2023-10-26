'''Task 4
Припустимо, що у тебе є дані про дружбу між користувачами соціальної мережі:
friendships = {
    "user1": {"user2", "user3", "user4"},
    "user2": {"user1", "user3"},
    "user3": {"user1", "user2", "user4"},
    "user4": {"user1", "user3"}
}
Напишіть програму для розрахунку спільних друзів у соціальній мережі, імена яких задає користувач.'''
friendships = {
    "user1": {"user2", "user3", "user4"},
    "user2": {"user1", "user3"},
    "user3": {"user1", "user2", "user4"},
    "user4": {"user1", "user3"}
}

a = input('введи имя первого друга (user1, user2, user3, user4)')
b = input('введи имя первого друга (user1, user2, user3, user4)')
if a == b:
    print('ты ввел одного и того же человека')
