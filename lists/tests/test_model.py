from django.core.exceptions import ValidationError
from django.test import TestCase
from lists.models import Item, List


class ItemAndListModelTest(TestCase):
    def test_saving_and_retrieving_item(self):
        new_list = List()
        new_list.save()

        first_item = Item() #call constructor as an instant no need for new like Java
        first_item.text = 'The first (ever) list item'

        #At this line, what is first_item.list???
        first_item.list=new_list
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list=new_list
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(new_list, saved_list)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(),2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(first_saved_item.list, new_list)
        self.assertEqual(second_saved_item.list, new_list)

    #we created an item within a new_list that has an empty text,
    #when we save the item, a validation error shoudl be raised
    #so that we don't save the item
    def test_cannot_save_empty_list_items(self):
        new_list = List.objects.create()
        item = Item(list=new_list, text='')

        #two ways to write this:
        #naive ways

        # try:
        #     item.save()
        #     self.fail('The save should have raised an exception')
        # except ValidationError:
        #     pass

        #instead:

        #if there are validation errors, save item
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()
