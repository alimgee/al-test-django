from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Item


class TestViews(TestCase):

    def test_get_home_page(self): # testing landing page load correctly
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200) # checking for status code 200
        self.assertTemplateUsed(page, "todo_list.html") # checking correct template loads
    
    def test_get_add_item_page(self): # testing /add loads
        page = self.client.get("/add")
        self.assertEqual(page.status_code, 200) # expecting status code 200
        self.assertTemplateUsed(page, "item_form.html") # expecting item form template to load
    
    def test_get_edit_item_page(self): # testing edit item
        item = Item(name="Create a Test") # create item and save
        item.save()

        page = self.client.get("/edit/{0}".format(item.id)) # storing item url
        self.assertEqual(page.status_code, 200) # expecting status code 200
        self.assertTemplateUsed(page, "item_form.html") # expecting item for template to load
    
    def test_get_edit_page_for_item_that_does_not_exist(self): # checking 404 loads when item does not exist in db
        page = self.client.get("/edit/1") # generating fake page url
        self.assertEqual(page.status_code, 404) # especting 404 status code
    
    def test_post_create_an_item(self): # checking item can be added with done set to false as default
        response = self.client.post("/add", {"name": "Create a Test"}) # posting dummy item
        item = get_object_or_404(Item, pk=1) # storing expected item
        self.assertEqual(item.done, False) # expecting false for done by default
    
    def test_post_edit_an_item(self): # test that the name field can be edited
        item = Item(name="Create a Test")
        item.save()
        id = item.id # creating a new item and passing to item var

        response = self.client.post("/edit/{0}".format(id), {"name": "A different name"})
        item = get_object_or_404(Item, pk=id) # posting an edit to name field

        self.assertEqual("A different name", item.name) # expecting the name field is now changed
    
    def test_toggle_status(self): #testing toggle 
        item = Item(name="Create a Test")
        item.save()
        id = item.id # creating item

        response = self.client.post("/toggle/{0}".format(id)) # posting created item with toggle

        item = get_object_or_404(Item, pk=id) # passing new item  with defalt done value (false)to item var
        self.assertEqual(item.done, True) # item toggle should now be set to true