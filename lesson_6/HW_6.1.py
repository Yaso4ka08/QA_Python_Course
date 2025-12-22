"""Порахувати кількість унікальних символів в строці.
Якщо їх більше 10 - вивести в консоль True, інакше - False.
Строку отримати за допомогою функції input()"""

user_input = input("Please enter the sentence here: ")

print(len(user_input)>10)
