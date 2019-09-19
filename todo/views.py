from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


# Create your views here.
def get_todo_list(request):
    results = Item.objects.all()# take all objects from db
    return render(request, "todo_list.html", {
        'items': results
    })# render in template


def create_an_item(request):
    if request.method == "POST":# if form is posted
        form = ItemForm(request.POST, request.FILES)# passing form created from models
        if form.is_valid():# validating and saving
            form.save()
            return redirect(get_todo_list) # redirect to landing if valid
    else:
        form = ItemForm() # otherwise reload form

    return render(request, "item_form.html", {'form': form}) # render form


def edit_an_item(request, id):
    item = get_object_or_404(Item, pk=id) # if item does not exist return 404

    if request.method == "POST": # if form is posted
        form = ItemForm(request.POST, instance=item) # pass current item
        if form.is_valid(): # if form vlaidates save to db and redirect to landing
            form.save()
            return redirect(get_todo_list)
    else:
        form = ItemForm(instance=item) # otherwise load form item again
    return render(request, "item_form.html", {'form': form}) # render form


def toggle_status(request, id):
    item = get_object_or_404(Item, pk=id)
    item.done = not item.done # toggle item done value to trueor false
    item.save() # save change and reload landing
    return redirect(get_todo_list)