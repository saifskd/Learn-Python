# pyrefly: ignore[missing-import]
import numpy as np
# 
# 
# 
# a = input("Enter a number: ");
# b = 30
# a = int(a);

# print(a+b);


# num = int(input("Enter your number: "));
# numtwo = int(input("Enter your second number: "));

# plushnum = num + numtwo;
# plushnum += 1000
# print(plushnum);

# print(10 <= 0 or 12 <= 8);

# So build a Student marks checker or tester program.

# studentNum = int(input("Enter Your Marks here: "));

# if studentNum >= 80: print("Good"); 
# elif studentNum < 80 and studentNum >= 55: print("Avreage, Not Bad");

# else: print("Try again next time...");


# NameofPerson = "Sundarikhukhad"

# print(NameofPerson.find("S"))

# fistNum = int(input("Enter Your Firt Number: " ))
# symblOfTheUser = input("Enter what you need to do?")
# secondNum = int(input("Enter Your 2nd Number: "))

# a = +
# b = -
# c = *
# b = /

# if symblOfTheUser == "a":
#     finalResunt = fistNum + secondNum

# elif symblOfTheUser == "b":
#     finalResunt = fistNum - secondNum

# elif symblOfTheUser == "c":
#     finalResunt = fistNum * secondNum

# elif symblOfTheUser == "b":
#     finalResunt = fistNum / secondNum

# else:
#     finalResunt = "The input is not velid!"

# print(finalResunt)

# newarr = range(1, 11)

# print(newarr)


# numOfprint = 0

# while numOfprint <= 20:
#     print("Saif Bhai")

#     numOfprint += 2

# print("The Loop is Ended")

# i = 1

# while i<=89:
#     print(i * "*")

#     i+=1

# print("//////////////////////")

for i in range(90, 901, 2):
    print(i)

for i in range(21):
    if(i % 3 == 0):
         print(i)

table = 57
while table < 570:
    if table != 570:
        print(table)
    table += 57

print("570")


# for cont in range(50):
#     if cont == 15:
#         continue

#     if cont % 3 == 0:
        # print(cont);


# sflist = [13, 24, 354, 464, 346, 35, 25, 46]

# sflist.insert(-1, 420)

# for aslist in sflist:
#     print(aslist) 

arr = np.arange(1, 11)

A_arr = np.arange(1, 51)

B_arr = np.arange(21, 71)

# AB_result = np.where(A_arr > 20, A_arr, B_arr)
# print(AB_result)


RandNum = np.random.randint(-20, 50, size=(5, 4))
print(RandNum)

Narr = np.array([[-10,  25,  12,  37],
 [ 42,   2,  14,  40],
 [ 16,  10,  45,  -4],
 [ 27,  40,   34,  47],
 [ 33, -12,   33,  40]])

print(np.any(Narr > 10, axis=0))
print(np.all(Narr > 10, axis=0))


## Shortlist / Matrix
arr1 = np.sort(RandNum, axis=1 )[::-1, ::]
arr1

arr2 = np.sort(RandNum, axis=1 ).reshape(4, 5)
arr2

def calculator():
    print("Simple Python Calculator")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    while True:
        choice = input("Enter choice (1/2/3/4) or 'q' to quit: ")

        if choice.lower() == 'q':
            print("Exiting calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            if choice == '1':
                print(f"Result: {num1} + {num2} = {num1 + num2}\n")

            elif choice == '2':
                print(f"Result: {num1} - {num2} = {num1 - num2}\n")

            elif choice == '3':
                print(f"Result: {num1} * {num2} = {num1 * num2}\n")

            elif choice == '4':
                if num2 == 0:
                    print("Error! Division by zero is not allowed.\n")
                else:
                    print(f"Result: {num1} / {num2} = {num1 / num2}\n")
        else:
            print("Invalid Input. Please select a valid option from 1 to 4.\n")

# Run the calculator
if __name__ == "__main__":
    calculator()


