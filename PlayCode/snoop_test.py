# For the video version of this, go here:
#     https://prosperousheart.com/python-visualizers
# ==================================================================
# snoop:  https://pypi.org/project/snoop
#         https://github.com/alexmojaki/snoop
#
# Looking for a powerful set of debugging tools without needing to
# know how to set it all up ... let alone have the time?
# Save time and your sanity by using snoop!
#
# With a single decorator line above the function you're interested
# in, you can get a play-by-play log of your function. Including
# which lines ran when & exactly when local variables were changed.
# No print or other logging required.
#
# Thanks to khuyentran1401 for the original snoop example!
# (I tweaked it to be more interactive.)
# https://gist.github.com/khuyentran1401/04b81b80e41ba9ce2aa2fda818aa9729#file-snoop_example-py
# ==================================================================

# ================================================
# Process for using snoop for catching errors:
# 1. run:  pip install snoop
# 2. in your code, add the following line:
#       import snoop
# 3. add the following decorator above your function(s):
#       @snoop
# ================================================
import snoop


@snoop
def factorial(x):
    if x == 1:
        return 1
    else:
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
