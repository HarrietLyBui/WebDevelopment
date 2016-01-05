from django.shortcuts import render

# Create your views here.
#function that does not do anything, makes the resolver happy
def home_page(request):
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text',''),
    })

    #this will break the functional test so don't do this
    #if request.method == 'POST':
        #return HttpResponse(request.POST['item_text'])
    #return render(request, 'home.html') #if it is not in a template folder


    # but in home folder home/home.html
