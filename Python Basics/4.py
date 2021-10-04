# input() - string 
# a = int("0")
# print(type(a))


# str + str -> string concatination 

# n = int(input("Enter n : "))
# print(n**(0.5))


# if else elif 

# age = int(input("Enter age : "))
# if age>18:
#     print("You can drive") 
# elif age == 18:
#     print("Liscense")
# else:
#     print("You cannt drive")


# total = int(input("Enter total price : "))
# if total>=1000:
#     pay = total - (total/100)*10
#     print(pay)
# elif total<1000 and total>=500:
#     pay = total - (total/100)*5
#     print(pay)
# else:
#     pay = total
#     print(pay)




# n = int(input("Enter n : "))
# if n%2==0:
#     print("Even")
# else:
#     print("Odd")


# a = int(input("Enter a : "))
# b = int(input("Enter b : "))
# if a>b:
#     print("A is greater")
# elif a<b:
#     print("B is greater")
# else:
#     print("Both are equal")



# n = int(input("Enter n : "))
# if n<0:
#     print("Negative")
# elif n>0:
#     print("Positive")
# else:
#     print("n=0")



# n = int(input("Enter n : "))
# if n == 999:
#     print("Winner")
# else:
#     print("Loser")



# n = int(input("Enter n : "))
# if n!=2:
#     print("Winner")
# else:
#     print("loser")

# a = input("Enter a letter : ")
# symbol = list("!@#%^(){}.,<>?[]~`")
# if "a" in symbol:
#     print("You enter symbol")
# else:
#     print("No symbol")



# a = input("Enter a sentence : ")
# listOfword = a.split()
# if len(listOfword)<=3:
#     print("invalid")
# else:
#     print("valild")


email = input("Enter emial : ")
if "@" in email and "." in email:
    print("valid") 
else:
    print("not valid")
