from django.shortcuts import render
from random import choice
# Create your views here.

def home(request):

    return render(request,'generator/home.html')

def password(request):

    chars=[chr(x) for x in range(97,123)]

    if(request.GET.get('Uppercase')=='on'):
        uppercase=[chr(x) for x in range(65,91)]
        chars.extend(uppercase)

    if(request.GET.get('Numbers')=='on'):
        numbers=[str(x) for x in range(0,9)]
        chars.extend(numbers)

    if(request.GET.get('SpecSymbols')=='on'):
        specsymbols= ['!','@','#','$','%','&']
        chars.extend(specsymbols)

    lenght=int(request.GET.get('lenght'))

    password=''


    for i in range(lenght):
        password+=choice(chars)

    return render(request,'generator/password.html',{'password':password})