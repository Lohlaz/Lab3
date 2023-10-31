import Lab2.Lab2 as bmi
#import the file then after the dot is the name of the .py file you wanna use for unit testing


print("Test_Lab3")


def test_Underweight():
    assert(-1 == bmi.calculate_bmi(height = 1.5, weight = 30)) # use the name that represent Lab2 up there and then . name of function you wish to test in Lab2.py


def test_Normalweight():
    assert(0 == bmi.calculate_bmi(height = 1.7, weight = 60))

def test_Overweight():
     assert(1 == bmi.calculate_bmi(height = 1.7, weight = 100))


