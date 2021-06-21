from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def validate(request):
    u_name = request.POST['username']
    p_word = request.POST['password']

    return render(request, 'userpage.html', {'username' : u_name})
