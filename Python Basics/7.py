# a = {
#     "Yash" : 2,

# }
# print(a)


# myList = (1,2,3,4)

# for i in range(20):
#     if i == 6:
#         break 
#     print(i)



# for item in range(10):
#     print(item)
#     if item == 5:
#         break 



# for i in range(0,12,2):
#     if i == 7:
#         break
#     print(i)



# for j in range(1,11,2):
#     if j == 4:
#         break
#     print(j)

# for i in range(0,12,2):
#     if i == 6:
#         break
#     print(i)


# for i in range(20):
#     print(i)
#     if i == 11:
#         break




# for i in range(20):
#     if i == 10:
#         break
#     print(i)


# for i in range(200):
#     print(i)
#     if i == 11:
#         break


# for i in range(20000):
#     if i == 19:
#         break
#     print(i)


# for i in range(200):
#     print(i)
#     if i == 32:
#         break

# for i in range(100):
#     if i == 31:
#         break
#     print(i)


# for i in range(1,100,2):
#     if i == 6:
#         break
#     print(i)


# for i in range(0,22,2):
#     if i == 14:
#         break
#     print(i)


# n = int(input("Enter n : "))
# primeHai = True
# for i in range(2,n,1):
#     if n%i==0:
#         primeHai = False
#         break
# if primeHai == True:
#     print("PRime")
# else:
#     print("Not prime")



# myList = [1,2,3,6,4]
# myList.sort()
# print(myList)



def isEven(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")

# isEven(11)



def isPrime(n):
    primeHai = True
    for i in range(2,n,1):
        if n%i==0:
            primeHai = False
            break 
    if primeHai == True:
        print("Prime")
    else:
        print("Not prime")


def printTable(n):
    for i in range(1,11,1):
        print(n*i)


def sayGoodMorning(name):
    print("Good morning", name)


# sayGoodMorning("Jayant")
# sayGoodMorning("yashveer")



# printTable(9)

# for i in range(200):
#     print(i)
#     if i == 19:
#         break

# function -> Code reuse 