from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from lists.models import Item,List

# Create your views here.
#function that does not do anything, makes the resolver happy
def home_page(request):
    return render(request, 'home.html', {'todo_lists': List.objects.all()})

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

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None

    if request.method == 'POST':
        if request.POST.has_key('item_text'):
            try:
                item = Item(text=request.POST['item_text'], list=list_)
                item.full_clean()
                item.save()
            except ValidationError:
                error = "You can't have an empty list item"

        if request.POST.has_key('list_name'):
            list_.name = request.POST['list_name']
            list_.save()

    return render(request, 'list.html', { 'list':list_, 'error': error })

# def add_item(request, list_id):
#     pass

def delete_item(request, list_id, item_id):
    list_ = List.objects.get(id=list_id)
    item=Item.objects.get(id = item_id)
    item.delete()
    return redirect('/lists/%d/' % (list_.id))

def edit_list(request, list_id):
    list_= List.objects.get(id=list_id)

    #iterate over the list of id
    #get all item out of the list
    for item in list_.item_set.all():
        item.is_done = False
        item.save()

    item_ids = request.POST.getlist('mark_item_done')

    for item_id in item_ids:
        item=Item.objects.get(id=item_id)
        item.is_done = True
        item.save()

    return redirect('/lists/%d/' % (list_.id))
