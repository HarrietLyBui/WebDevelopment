from django.shortcuts import render

# Create your views here.
#function that does not do anything, makes the resolver happy
def home_page(request):
    return render(request, 'home.html') #if it is not in a template folder
    # but in home folder home/home.html
