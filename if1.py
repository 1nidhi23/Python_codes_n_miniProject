is_female = True

if is_female:
    print("You are a Female")
is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a male and you are tall.")
elif is_male and not (is_tall):
    print("You are a short male.")
elif not (is_male) and is_tall:
    print("You are not a male but tall.")
else:
    print("You are neihter male nor tall.")

#Comaprision

def max_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_number(30, 58, 90))