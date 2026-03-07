# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

lst = [2,4,3,8,34,78,23,1,45,1.4,2.43,100]
evens_from_lst = []
# adding each even element from lst to evens_from_lst list
[evens_from_lst.append(x) for x in lst if x % 2 == 0]

# calculation of sum of each iterable element in our list with even numbers
sum_of_evens = sum(evens_from_lst)

print(sum_of_evens)