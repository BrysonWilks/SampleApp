from django.shortcuts import render
from . import models

# Create your views here.
def home(request):
    return render(request, 'home.html')


def validate(request):
    u_name = request.POST['username']
    p_word = request.POST['password']

    #Creating a user for test purposes
    U1 = models.User()
    U1.username = "Bob1234"
    U1.password = "password"

    if u_name == U1.username and p_word == U1.password:
        return render(request, 'userpage.html', {'username' : u_name})
    else:
        return render(request, 'home.html', {'error_message': 'Incorrect credentials please try again'})
