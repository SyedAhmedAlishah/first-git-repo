def say_hi(name, age, field):
    print("My naame is " + name)
    print("i am "+str(age)+" years old")
    print("i am an "+field+" student")


say_hi("Ahmed", 21, "Engineering")


def cube(num):
    print("\nthis prints")
    return num**3  # after return nothing would print


print(cube(4))
print("//////////////numbers comparison///////////")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print("maximun number is= ", max_num(10, 5, 1))
print("\n//////////////String comparison///////////")


def str_comparison(str1, str2):
    if str1 == str2:
        print("you have logged in to your account")
    else:
        print("Sorry wrong password\naccess denied")


stroed = "pakistan.1234"
password = input("enter your password: ")
str_comparison(stroed, password)
