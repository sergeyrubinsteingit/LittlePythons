given_int: int= 205
reverse_int: int = 0 # Must have a value to start process with

while given_int > 0:
    reminder_ = given_int % 10
    reverse_int = (reverse_int * 10) + reminder_
    given_int = given_int // 10

print("reverse_int = " + str(reverse_int))
###################################################################################
# ALGO:
# reminder_ = given_int % 10 -> Separates the last digit of the given integer;
# (reverse_int * 10) -> Adds this digit to reverse integer and moves it one register up;
# given_int = given_int // 10 -> Clears up the last digit in given integer till
#                               this integer becomes 0; then the process stops.

