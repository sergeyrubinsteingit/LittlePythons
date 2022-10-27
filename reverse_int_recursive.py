def reverse_int(giv_int_):
    global revr_int_
    if giv_int_ > 0:
        revr_int_ = (revr_int_ * 10) + (giv_int_ % 10)
        giv_int_ = giv_int_ // 10
        reverse_int(giv_int_)
    else:
        return


given_int_ = 4546
revr_int_ = 0
reverse_int(given_int_)

print(revr_int_)
###################################################################################
# ALGO:
# (giv_int_ % 10) -> Separates the last digit of the given integer;
# (revr_int_ * 10) -> Adds this digit to reverse integer and moves it one register up;
# giv_int_ = giv_int_ // 10 -> Clears up the last digit in given integer till
# this integer becomes 0; then the function stops.

