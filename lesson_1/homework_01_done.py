# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4

# task 05 == виправте назви змінних
left_side = 1
right_side = 2
bottom_side = 3
top_side = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimeter = sum([left_side,right_side,bottom_side,top_side])
print(perimeter)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apple_trees = 4
pear_trees = apple_trees + 5
plum_trees = apple_trees - 2
overall_trees = sum([apple_trees, pear_trees, plum_trees])
print(f"There were {apple_trees} apple trees planted in the garden. The pear trees were 5 more than apple trees - {pear_trees}, "
      f"and the plum trees 2 less than apple trees - {plum_trees}")
print(f"Overall, {overall_trees} trees were planted in the garden.")

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
# Подивимось яка температура буде надвечір, але ось тиск та головна біль точно була б

morning_temperutre = 5
afternoon_temperature = morning_temperutre -10
evening_temperature = afternoon_temperature +4
print(f"Надвечір температура зараз {evening_temperature}C.")

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys = 24
girls = int(boys/2)
today_attendent_boys = boys -1
today_attendent_girls = girls-2
all_attendent_kids = today_attendent_boys + today_attendent_girls
print(f"Today we have {all_attendent_kids} kids in our theatre group.")

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""

first_book = 8
second_book = first_book + 2
third_book = (first_book+second_book)/2
all_books = sum([first_book,second_book,third_book])
print(f"All books will cost you  {all_books} UAN.")