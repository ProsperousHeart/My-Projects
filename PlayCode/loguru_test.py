# For the video version of this, go here:
#     https://prosperousheart.com/python-visualizers
# ==================================================================
# Loguru:  https://github.com/Delgan/loguru
#
# Loguru is a library that aims to improve logging in Python.
# It provides many interesting functionalities, including
# the ability to catch unexpected errors and display which value
# causes your code to fail.
#
# Thanks to khuyentran1401 for this loguru example!
# https://gist.github.com/khuyentran1401/259c326aaadd1c7c69a3a733072d83bf#file-loguru_example-py
# ==================================================================

# ================================================
# Process for using Loguru for catching errors:
# 1. run:  pip install loguru
# 2. in your code, add the following line:
#       from loguru import logger
# 3. add the following decorator above your function(s):
#       @logger.catch
# ================================================

# from loguru import logger

# https://docs.python.org/3/library/itertools.html#itertools.combinations
from itertools import combinations

def division(num1: int, num2: int):
    return num1/num2

# @logger.catch
def divide_numbers(num_list: list):
    """Division of 2 numbers in the number list """

    for comb in combinations(num_list, 2):
        num1, num2 = comb
        res = division(num1, num2)
        print(f"{num1} divided by {num2} is equal to {res}.")


if __name__ =='__main__':
    num_list = [2, 1, 0]
    divide_numbers(num_list)
