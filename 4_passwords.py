# https://adventofcode.com/2019/day/4

# six digit password
# The value is within the range given in your puzzle input. (372037-905157)
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease;

# second round:
# the two adjacent matching digits are not part of a larger group of matching digits.

UPPER_BOUND = 905157
LOWER_BOUND = 372037

def two_adjacent_are_the_same(password):
    return password[0] == password[1] or password[1] == password[2] or password[2] == password[3] or password[3] == password[4] or password[4] == password[5]

def two_adjacent_are_the_same_no_groups(password):
    return ((password[0] == password[1] and password[1] != password[2]) or
            (password[1] == password[2] and password[1] != password[0] and password[2] != password[3]) or 
            (password[2] == password[3] and password[2] != password[1] and password[3] != password[4]) or 
            (password[3] == password[4] and password[3] != password[2] and password[4] != password[5]) or 
            (password[4] == password[5] and password[4] != password[3]))

def never_decrease(password):
    return password[0] <= password[1] and password[1] <= password[2] and password[2] <= password[3] and password[3] <= password[4] and password[4] <= password[5]
 
def check_for_consistency(password):
    int_password = password
    password = str(password)
    return (len(password) == 6 and 
            int_password <= UPPER_BOUND and 
            int_password >= LOWER_BOUND and 
            two_adjacent_are_the_same(password) and 
            never_decrease(password) and 
            two_adjacent_are_the_same_no_groups(password))

# assert(check_for_consistency(444444) == True)
assert(check_for_consistency(223450) == False)
assert(check_for_consistency(123789) == False)

print(sum(map(check_for_consistency, range(LOWER_BOUND, UPPER_BOUND))))
