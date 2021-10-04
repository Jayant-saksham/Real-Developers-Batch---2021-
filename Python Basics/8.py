# Revision 

# print("Kabir", "Manu", "Roshni")


# name = 'Manu'
# std = '12'
# print("My name is", name, "and i study in ", std, "Class")
# print(f"My name is {name} and I study in {std} class")

# n = int(input("Enter n : "))
# for i in range(1,11,1):
#     print(f"{n} x {i} = {n*i}")



# int, float, string, bool, list, tuple, dict 
# myD = {
#     'First' : 1,
#     'Second' : 2
# }
# del myD['First']
# myD['Jayant'] = "python"
# print(myD['First'])


# import random
# print(random.randint(2,4))

# import random
# myTuple = (1,2,3,4,5,56)
# print(random.choice(myTuple))


# sentence = input("Enter sentence : ")
# listOfword = sentence.split()
# print(listOfword[0])


# sentence = input("Enter sentence : ")
# listofword = sentence.split()
# print(len(listofword))


# print(len(input("Enter sentence : ").split()))

# def textAnalyzer(sentence):
#     space = 0
#     smallLetter = 0
#     capitalLetter = 0
#     symbol = 0
#     number = 0
#     for i in sentence:
#         if i == ' ':
#             space = space + 1
#         elif i.isupper():
#             capitalLetter = capitalLetter + 1
#         elif i.islower():
#             smallLetter = smallLetter + 1
#         elif i.isnumeric():
#             number = number + 1
#         else:
#             symbol = symbol + 1 

#     print(f"Symbol {symbol} Cap {capitalLetter} small {smallLetter} number {number} space {space}")



# sentence = input("Enter sentence : ")




# def function():
#     return "Hello"
#     print("This is mee")

# print(function())


# def isEven(n):
#     if n%2==0:
#         return True
#     return False

# a = isEven(5)
# print(a)


# def emailSender():
#     return "Email.html"

# def isEven(n):
#     if n%2==0:
#         return True
#     return False

# myList = [1,2,3,4,5,6]
# for i in myList:
#     if isEven(i):
#         print(i)


def isPrime(n):
    flag = True
    for i in range(2,n,1):
        if n%i==0:
            flag = False
            break
    if flag == True:
        return True
    return False


n = int(input("Enter n : "))
for i in range(2,n+1,1):
    if isPrime(i):
        print(i)
