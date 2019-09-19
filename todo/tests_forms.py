from django.test import TestCase
from .forms import ItemForm # importing form from forms.py for tests

# Create your tests here.
class TestToDoItemForm(TestCase):

    def test_can_create_an_item_with_just_a_name(self):
        form = ItemForm({'name': 'Create Tests'}) # create form with name
        self.assertTrue(form.is_valid()) # check if valid
    
    def test_correct_message_for_missing_name(self):
        form = ItemForm({'form': ''}) # create form with no name
        self.assertFalse(form.is_valid()) # valid should return false
        self.assertEqual(form.errors['name'], [u'This field is required.']) 
        # checking correct error message