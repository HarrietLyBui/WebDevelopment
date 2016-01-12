
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
