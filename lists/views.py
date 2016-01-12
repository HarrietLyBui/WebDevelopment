from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from lists.models import Item,List

# Create your views here.
#function that does not do anything, makes the resolver happy
def home_page(request):
    return render(request, 'home.html')

    #if request.method == 'POST':
    #    Item.objects.create(text=request.POST['item_text'])
        #new_item_text = request.POST['item_text']
        #Item.objects.create(text=new_item_text)
        #return redirect('/lists/the-only-list/')
    #else:
    #    new_item_text = ''
    #item = Item()
    #item.text = request.POST.get('item_text','')
    #item.save()

    #create new item everytime we go to homepage so that is very bad
#    items = Item.objects.all()
    #this will break the functional test so don't do this
    #if request.method == 'POST':
        #return HttpResponse(request.POST['item_text'])
    #return render(request, 'home.html') #if it is not in a template folder


    # but in home folder home/home.html

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', { 'list':list_ })

def new_list(request):
    new_list = List.objects.create()
    item = Item(text=request.POST['item_text'], list=new_list)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        new_list.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {'error': error})
    return redirect('/lists/%d/' % (new_list.id))

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id))
def delete_item(request, list_id, item_id):
    list_ = List.objects.get(id=list_id)
    item=Item.objects.get(id = item_id)
    item.delete()
    return redirect('/lists/%d/' % (list_.id))
