from django.shortcuts import render, redirect
from lists.models import Item

# Create your views here.
#function that does not do anything, makes the resolver happy
def home_page(request):

    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        #new_item_text = request.POST['item_text']
        #Item.objects.create(text=new_item_text)
        return redirect('/lists/the-only-list/')

    #else:
    #    new_item_text = ''


    #item = Item()
    #item.text = request.POST.get('item_text','')
    #item.save()

    #create new item everytime we go to homepage so that is very bad
    items = Item.objects.all()

    return render(request, 'home.html')

    #this will break the functional test so don't do this
    #if request.method == 'POST':
        #return HttpResponse(request.POST['item_text'])
    #return render(request, 'home.html') #if it is not in a template folder


    # but in home folder home/home.html

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
