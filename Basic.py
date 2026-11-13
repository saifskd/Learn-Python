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

def first_plus(num):
  if num % 2 == 0:
    return "This is a Even Number"

  else:
    return "This is a Odd Number"


rand_num = np.random.randint(0, 100, 1000000)
rand_num.size


import numpy as np

# A mock dataset of 100 samples
data = np.arange(100)

# Split at index 60 and 80 to create a 60% / 20% / 20% split
train, val, test = np.split(data, [60, 80])
train, val, test
import numpy as np
new2darr = np.arange(1, 17).reshape(4, 4)

np.split(new2darr, 2, axis=0)

import numpy as np
np.array_split(new2darr, 2, axis=1)

np.hsplit(new2darr, 1)

np.hstack([a, b])


np.vstack([a, b])
np.concatenate([a, b])


import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

df.head(20) ## For see top row data

## stands for "location" (label-based indexing) and iloc stands for "integer location" (position-based indexing)
df.iloc[0:20: 2] ## For checking index wize

df_explicit = df.set_index("species")
df_explicit.iloc[0:-1: 7]

df_explicit.loc["virginica"]

df_explicit.iloc[0:4, 0:2]


df["petal_length"].value_counts()

df["petal_length"].value_counts().reset_index().head() ## For reset the index and get top 5 rows


df["species"].nunique() ## To find the unique velues in the list of data fram

## Date 9-11-2026 

df["petal_width"].min()

df["petal_width"].max()

df["petal_width"].mean()


df[["petal_width", "sepal_length", "sepal_width"]].agg(["min", "mean", "max"])

df.sort_values(["petal_width", "sepal_width"], ascending=[False, True]).reset_index(drop=True)

newdf = df.rename(columns={"sepal_length": "Rating"}).sort_values("Rating", ascending=False).tail().reset_index(drop=True)

## Dataframe df1 and df2 marging learing:-


df1 = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                    111, 112, 113, 114, 115],
    "Name": ["Saif", "Rahul", "Aman", "Priya", "Rohit",
             "Neha", "Vikas", "Anjali", "Karan", "Sneha",
             "Arjun", "Pooja", "Mohit", "Riya", "Varun"],
    "Age": [22, 25, 24, 23, 27, 26, 29, 22, 28, 24,
            30, 25, 27, 23, 26],
    "Salary": [25000, 30000, 28000, 35000, 32000,
               27000, 40000, 26000, 38000, 31000,
               45000, 29000, 36000, 33000, 41000],
    "Department_ID": [1, 2, 3, 1, 2, 4, 3, 5, 2, 4,
                      6, 1, 5, 3, 7]
})

df2 = pd.DataFrame({
    "Department_ID": [1, 2, 3, 4, 5, 6, 8, 9],
    "Department_Name": [
        "IT", "HR", "Marketing", "Finance",
        "Sales", "Development", "Design", "Support"
    ],
    "Location": [
        "Delhi", "Mumbai", "Noida", "Gurgaon",
        "Faridabad", "Pune", "Jaipur", "Chandigarh"
    ]
})

def clean_price(df, column):
    df[column] = pd.to_numeric(
        df[column].astype(str).str.replace(r"[₹,$,]", "", regex=True).str.strip(),
        errors="coerce"
    )
    return df

# Usage:
    df = clean_price(df, "Price")


    df.groupby("location")["votes"].mean().reset_index()

    df.groupby(["name", "location"])["votes"].sum().reset_index()

    df.isnull().sum()

    df["votes"].fillna(df["votes"].mean()) ## this function will fill all null values with mean values


df_cut = df[["name", "votes"]]

df_cuting = pd.cut(
    df_cut["votes"],
    bins=[20, 120, 220, 440, 800],
    labels=["low", "mid", "normal", "high"]
)
