from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class TodoFunctionalTest(StaticLiveServerTestCase): #extend unittest

    def setUp(self): #method within class

        self.browser = webdriver.Firefox() #open firefox before any test
        self.browser.implicitly_wait(3) #if nothing happens, wait three second and close

    def tearDown(self):

        self.browser.quit() #close the browser after every test

    def find_table_row(self, item_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        for row in rows:
            row_text = row.find_element_by_css_selector('.content').text
            if item_text == row_text:
                return row
        self.fail('"%s" not in table - "%s"' % (item_text, table.text))

    def check_for_row_in_list_table(self, row_text):
        row = self.find_table_row(row_text)
        self.assertIsNotNone(row)

    def enter_a_new_item(self, todo_text):
        inputbox = self.browser.find_element_by_id('id_new_item') #create an input box
        inputbox.send_keys(todo_text) #get user input
        inputbox.send_keys(Keys.ENTER) #automatically press enter
