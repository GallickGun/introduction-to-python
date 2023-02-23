# concatenate
first_name = 'Gallick'
last_name = 'Gun'
full_name = first_name + last_name

print(full_name)

# count string length

length = len(full_name)
print(length)

# check char in a string

part = 'Gall'
check = part in full_name #not in or in
print(check)

#repetition
print('hi'*5)
print(2*'hi')

# indexing
print(full_name[1])
print(full_name[0:4])

# 
data = "Gallick"
result = data.count("k")
print(result)

#uppercase
greeting = "hiya!"
greeting = greeting.upper()
print(greeting)

#lowercase
sentence = "I AM GaLLick gUN"
sentence = sentence.lower()
print(sentence)

#isX method
title = "QA Engineer"
is_lowercase = title.islower()
print(is_lowercase)
is_uppercase = title.isupper()
print(is_uppercase)

is_title = title.istitle()
print(is_title)

#join
team_one = ['Goku', 'Trunks'] 
join_team = ' '.join(team_one)
print(join_team)
