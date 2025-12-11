# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
print("Task #1")
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    result = 0

    # Complete the while loop condition.
    while result <= 25 :
        result = number * multiplier
        # десь тут помилка, а може не одна
        if  result <= 25:
            print(f"{number}x{multiplier}={result}")

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
print()
print("Task #2")
def sum_of_two_numbers(a,b):
    result = a + b
    return result
#To see if it works
print(sum_of_two_numbers(2,9))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
print()
print("Task #3")
def arithmetic_mean(*args):
    arith_mean = sum(args)/len(args)
    return arith_mean
#To see if it works
print(arithmetic_mean(2,3,4))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
print()
print("Task #4")
def reverse_string(*args):
    rever_str = []
    for s in args:
        if not isinstance(s, str):
            print(TypeError(f"{s} is not string"))
            continue
        rever_str += [s[::-1]]
    return rever_str
#To see if it works
print(reverse_string("terra", 637, "toop"))


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
print()
print("Task #5")
def the_longest_word(*args):
    longest = max(args, key=len)
    return longest
#To see if it works
print(the_longest_word("test", "whoo-hoo", "chumba"))
# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
print()
print("Task #6")
def find_substring(str1, str2):
    sub_str = str1.find(str2, 0, len(str1))
    return sub_str

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# function to count how many symbols in the inputted string and if it is more than 10 - print True,
# otherwise - False
print()
print("Task #7")
def string_count(str):
    print(len(str)>10)
#To see if it works

string_count(input("Please enter the sentence here: "))

# task 8
print()
print("Task #8")
"""Function to ask user to enter word with 'h' inside it. It should run until user entered the right word."""
def checking_if_h_in_the_word(a):
    while "h" not in a.lower():
        a = input("Please enter a word that contains 'h' letter: ")
    print("Finished")
#To see if it works
print(checking_if_h_in_the_word("someting"))

# task 9
print()
print("Task #9")
"""Getting a list of variables and we need to create a new one only with gotten strings"""
def strings_only_list(a):
    lst2 = []
    for x in a:
        if isinstance(x, str):
            lst2.append(x)
    return lst2

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
#To see if it works
print(strings_only_list(lst1))

# task 10
print()
print("Task #10")
def sum_of_evens_from_list(a):
    evens_from_lst = []

    # adding each even element from lst to evens_from_lst list
    [evens_from_lst.append(x) for x in lst if x % 2 == 0]

    # calculation of sum of each iterable element in our list with even numbers
    sum_of_evens = sum(evens_from_lst)

    return sum_of_evens

lst = [2,4,3,8,34,78,23,1,45,1.4,2.43,100]

print(sum_of_evens_from_list(lst))
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""