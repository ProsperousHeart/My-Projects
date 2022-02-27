# For the video version of this, go here:
#     https://prosperousheart.com/python-visualizers
# ==================================================================
# heartrate:  https://github.com/alexmojaki/heartrate
#
# This library package offers a simple, real time visualization of the
# execution of a python program. It shows how many times a line has been hit,
# what's been hit recently, highlights calls currently being executed,
# and evn shows a live stack trace!
#
# Thanks to khuyentran1401 for the example code!
# (I tweaked it to be more robust.)
# https://gist.github.com/khuyentran1401/5392270cae154fd0f552b53d3782d7d1#file-heartrate_example-py
# ==================================================================

# ================================================
# Process for using snoop for catching errors:
# 1. run:  pip install heartrate
# 2. in your code, add the following line:
#       import heartrate
# 3. add the following line underneath import:
#       heartrate.trace(browser=True)
# ================================================
from time import sleep
import heartrate
heartrate.trace(browser=True)

def factorial(x):
    if x == 1:
        return 1
    else:
        sleep(0.5)
        return (x * factorial(x-1))


if __name__ == "__main__":
    while True:
        try:
            num = int(input("What number >= 0 would you like to see a factorial of?\t"))
        except ValueError as err:
            print("Please provide an integer >= 0.")
        else:
            if num <= 0:
                print("Please provide an integer greater than 0.")
            else:
                break
    print(f"The factorial of {num} is {factorial(num)}")
