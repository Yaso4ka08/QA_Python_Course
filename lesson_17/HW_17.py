# Block #1 - Standard library (build-in)

import os
print(os.getcwd())

import math
print(math.sqrt(16))

import datetime
print(datetime.date.today())

import random
print(random.randint(1, 10))

import time
time.sleep(2)
print("done!")


# Block #2 - import via installing 3d party libraries
import requests
r = requests.get("https://google.com")
print(r.status_code)

import numpy as np
arr = np.array([1, 2, 3])
print(arr)

import pandas as pd
df = pd.DataFrame({"name": ["Alice", "Bob"]})
print(df)

import flask as fl
app = fl.Flask(__name__)
print("Flask app created!")

# import pytest
# @pytest.mark.parametrize("a,b",[
#     (1,4),
#     (2,-7)
# ])
# def test_sum(a,b):
#     assert a + b >= 5

# Block #3 - import my own modules

import lesson_1.HW_1 as hw_1
print(f"Today we have {hw_1.all_attendent_kids} kids in our theatre group.")

import lesson_10.HW_10_2 as hm_10
my_circle = hm_10.Circle(34)
print(f"The Circle area is {my_circle.calculate_area()}")


import lesson_8.HW_8 as hw_8
print(hw_8.Student)

import lesson_5.HW_5_2 as hw_5
print(hw_5.people_records)

import lesson_9.HW_9 as hw_9
print(hw_9.my_rhombus)

# Block #4 - importing specific parts

from math import pi
print(pi)

from os import getcwd
print(getcwd())

from random import choice
print(choice(["alfa-romeo", "ford", "toyota"]))

from datetime import date
print(date.today())

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://google.com")
print(driver.title)
driver.quit()


