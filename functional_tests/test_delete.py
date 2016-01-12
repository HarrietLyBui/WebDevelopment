from .base import TodoFunctionalTest

class DeleteItemTest(TodoFunctionalTest):
    def test_delete_items(self):
        self.browser.get(self.live_server_url)
        self.enter_a_new_item('Itemey 1 to delete') #create a new item
        self.enter_a_new_item('Itemey 2 to delete') #create a new item

        self.user_chooses_to_delete('Itemey 1 to delete')#delete an item

        import time
        #time.sleep(10)
        page = self.browser.find_element_by_tag_name('body')
        self.assertNotIn('Itemey 1 to delete', page.text )


    def user_chooses_to_delete(self, todo_text):
        table = self.browser.find_element_by_id('id_list_table')
        items = table.find_elements_by_tag_name('tr')
        for item in items:
            if todo_text in item.text:
                item.find_element_by_tag_name('a').click()
                return
