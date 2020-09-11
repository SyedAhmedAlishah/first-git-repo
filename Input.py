# NAME = input("Enter your Name :")
# AGE = input("Enter your Age :")
# print("Hi Mr "+NAME+"\nYou are "+str(AGE)+" years old")

NUM_1 = input("Enter 1st number ")
NUM_2 = input("Enter 2nd number ")
result=NUM_1+NUM_2
print(result)
print("//////////////METHOD 1 ////////// ")
NUM_1 = input("Enter 1st number ")
NUM_2 = input("Enter 2nd number ")
result = int(NUM_1) + int(NUM_2)    # numbers must be integer not float
print(result)
print("//////////////METHOD 2 ////////// ")
NUM_1 = input("Enter 1st number ")
NUM_2 = input("Enter 2nd number ")
result = float(NUM_1) + float(NUM_2)
print(result)