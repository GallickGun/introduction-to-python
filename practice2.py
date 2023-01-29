# ++++++3 ------ 10+++++++
inputUser = float(input('Input a number that is less than 3 or more than 10:'))
validInput = (inputUser < 3 or inputUser > 10)
print('Your input is', validInput)


# -----3++++++10-------
inputUser = float(input('Input a number that is more than 3 and less than 10:'))
validInput2 = (inputUser > 3 and inputUser < 10)
print('Your input is', validInput2)


# Homework
# 1. ---- 0 ++++++++ 5 ------- 8 +++++++ 11--------
# more than 0 less than 5 or more than 8 more than 11

inputUser = float(input('Input a number that is more than 0 and less than 5 or more than 8 and less than 11:'))
validInput3 = (inputUser > 0 and inputUser < 5 or  inputUser > 8 and inputUser < 11)
print('Your input is', validInput3)

#2. +++++ 0 ------- 5 ++++++++ 8 -------- 11 ++++++++
# before 0, between 5-8 or more than 11
inputUser = float(input('Input a number that is before 0, between 5 - 8 or more than 11:'))
validInput4 = (inputUser < 0 or inputUser >= 5  and inputUser <= 8 or inputUser > 11)
print('Your input is', validInput4)

