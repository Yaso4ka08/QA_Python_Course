adventures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adventures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adventures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
print("Task #1")
adventures_of_tom_sawer = adventures_of_tom_sawer.replace("\n"," ")
print(adventures_of_tom_sawer)


# task 02 ==
""" Замініть .... на пробіл
"""
print()
print("Task #2")
adventures_of_tom_sawer = adventures_of_tom_sawer.replace("...."," ")
print(adventures_of_tom_sawer)
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print()
print("Task #3")
adventures_of_tom_sawer = adventures_of_tom_sawer.replace("   ", " ")
print(adventures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print()
print("Task #4")
print(f"{adventures_of_tom_sawer.count("h")} times you can see the letter 'h' in the text above.")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print()
print("Task #5")
words = adventures_of_tom_sawer.split()
count_upper = 0
for i in words:
    if i[0].isupper():
        count_upper +=1
print(f"There are {count_upper} words started with the capital letter.")
# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print()
print("Task #6")
# finding the first time when we see Tom and adding 3 to the index because our word contains 3 letters
first_time_Tom = adventures_of_tom_sawer.find("Tom", 0)+3
second_time_Tom = adventures_of_tom_sawer.find("Tom", first_time_Tom)
print(f"You can find Tom at the second time in the text at {second_time_Tom} index.")
# task 07
""" Розділіть змінну adventures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
print()
print("Task #7")
adventures_of_tom_sawer_sentences = None
adventures_of_tom_sawer_sentences = adventures_of_tom_sawer.split(".")
# because instead of separator Python creates empty space I am deleting the last element of the list to avoid missleads.
if adventures_of_tom_sawer_sentences[-1] == "":
    adventures_of_tom_sawer_sentences.pop()
# List comprehension to make it clear and easy to use in the future
adventures_of_tom_sawer_sentences = [s.strip() for s in adventures_of_tom_sawer_sentences]
print(adventures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print()
print("Task #8")
forth_sentence = adventures_of_tom_sawer_sentences[3]
print(forth_sentence.lower())
# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print()
print("Task #9")
for i in adventures_of_tom_sawer_sentences:
    if i.startswith("By the time"):
        print(i)
# task 10
""" Виведіть кількість слів останнього речння з adventures_of_tom_sawer_sentences.
"""
print()
print("Task #10")
# to get the last index of the list
last_sentence = len(adventures_of_tom_sawer_sentences)-1
# all words from the last element in the list
words = adventures_of_tom_sawer_sentences[last_sentence]
# creating a new list with separated words from the last element in the parent list
word = words.split(" ")
count_of_words = len(word)
print(count_of_words)
