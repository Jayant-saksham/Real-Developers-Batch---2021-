from django.shortcuts import render
import random

def logic(n, isUpper, isNumber, isSymbol):
    choice_I_have = list("abcdefghijklmnopqrstuvwxyz")
    if isUpper == 'on':
        newList = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        choice_I_have.extend(newList)
    
    if isNumber == 'on':
        newList = list("0123456789")
        choice_I_have.extend(newList)
    
    if isSymbol == 'on':
        newList = list("!@#$%^&*()_{}[]~`'/|\-")
        choice_I_have.extend(newList)
    
    password = ""
    for i in range(n):
        x = random.choice(choice_I_have)
        password = password + x 
    
    return password



def home(request):
    return render(request, 'index.html')

def password(request):
    if request.method == "GET":
        number = request.GET.get('number')
        upper = request.GET.get('uppercase')
        symbol = request.GET.get('symbol')
        length = int(request.GET.get('length'))
        password = logic (
            n = length, 
            isUpper = upper, 
            isNumber = number, 
            isSymbol = symbol
        )
        data = {'pass' : password}

        
    return render(request, 'password.html', data)