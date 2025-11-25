print("Tasks 1-3")
alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n'
                       '"I don\'t much care where ——" said Alice.\n'
                        '"Then it doesn\'t matter which way you go," said the Cat.\n"'
                        '"—— so long as I get somewhere," Alice added as an explanation.\n"'
                        'Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')
print(alice_in_wonderland)
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

print()
"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
print("Task 4")
black_sea = 436402
azov_sea = 37800
both_seas = black_sea+azov_sea
print(f"Black and Azov seas have {both_seas} km2")
print()
# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
print("Task 5")
# total items for all warehouses
all_warehouses = 375291

# total items for the first and second warehouses
first_and_second_warehouses = 250449

# total items for the second and third warehouses
second_and_third_warehouses = 222950

# calculation of how many items does third warehouse has
third_warehouse = all_warehouses - first_and_second_warehouses

# calculation of how many items does second warehouse has
second_warehouse = second_and_third_warehouses - third_warehouse

# calculation of how many items does first warehouse has
first_warehouse = first_and_second_warehouses - second_warehouse

print(f"All warehouses have {all_warehouses} items. The first one has {first_warehouse} items, "
      f"second one - {second_warehouse},"
      f" and the third one has {third_warehouse}.")
print()
# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
print("Task 6")
credit_duration_months = 18
credit_payment_per_month = 1179
total_item_price = credit_payment_per_month * credit_duration_months

print(f"The laptop will cost {total_item_price} after {credit_duration_months} months of credit with a "
      f"{credit_payment_per_month} UAN payment a month.")
print()

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print("Task 7")
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print(a, b, c, d, e, f)
print()
# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
print("Task 8")
# price for the big pizza
big_pizza = 274
total_big_pizza = big_pizza * 4

# price for the medium pizza
medium_pizza = 218
total_med_pizza = medium_pizza * 2

# price for the juice
juice = 35
total_juice = juice * 4

# price for a cake
cake = 350
total_cake = cake

# price for the water bottles
water = 21
total_water = water * 3

# total price for the whole order
overall = total_juice + total_water + total_cake + total_med_pizza + total_big_pizza
print(f"You will need to pay {overall} UAN for the whole order.")
print()
# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
print("Task 9")
photos = 323
photo_places = 8

total_photo_pages = photos//photo_places

# in case if we have not even count of photos
additional_page = photos % photo_places
if additional_page > 0:
    total_photo_pages +1

print(f"Overall Ihor will need {total_photo_pages} pages to fit all the {photos} photos")
print()
# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-св
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
print("Task 10")
distance = 1600
gas_tank = 48
# calculation how many gas liters will we need for the journey
total_gas = int(distance / 100 * 9)

# minimum of stops to fuel your tank fully during the journey
min_gas_stops = total_gas//gas_tank

print(f"The whole journey takes {distance} km. With spending 9L/100km you will need {total_gas} liters of gas. "
      f"It means you are going to make {min_gas_stops} minimum stops to fuel your tank up to full to finish the journey.")
