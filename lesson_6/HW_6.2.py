"""Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h" (
враховуються як великі так і маленькі).
Цикл не повинен завершитися, якщо користувач ввів слово без букви "h"."""

user_input = ""

while "h" not in user_input.lower():
    user_input = input("Please enter a word that contains 'h' letter: ")

print("Finished")