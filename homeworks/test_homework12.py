import pytest
import HW_12

@pytest.mark.parametrize("values, expected", [
    ((2,4,6),4),
    ((10,40,40), 30),
    ((-1,0,1), 0)]
)
def test_arithmetic(values, expected):
    assert HW_12.arithmetic_mean(*values) == expected


# My tests here are failing because of comparison string and list. Where should I fix it?
# I belive inside the test or my function is wrong?
@pytest.mark.parametrize("values, expected", [
    ("test", "tset"),
    ("Abba", "abbA"),
    (123, "123 is not string"),
    (1.2, "1.2 is not string")
])
def test_reverse_string(values, expected):
    assert HW_12.reverse_string(values) == expected

@pytest.mark.parametrize("values", [
    "Harold",
    "who",
    pytest.param("test", marks=pytest.mark.xfail(reason="No 'h' in word"))
])
def test_if_h_inside_a_word(values):
    assert HW_12.checking_if_h_in_the_word(values) == "Finished"

