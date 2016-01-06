from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase): #extend unittest

    def setUp(self): #method within class

        self.browser = webdriver.Firefox() #open firefox before any test
        self.browser.implicitly_wait(3) #if nothing happens, wait three second and close



    def tearDown(self):

        self.browser.quit() #close the browser after every test
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def enter_a_new_item(self, todo_text):
        inputbox = self.browser.find_element_by_id('id_new_item') #create an input box
        inputbox.send_keys(todo_text) #get user input
        inputbox.send_keys(Keys.ENTER) #automatically press enter

    #Now we refractor the above code
    def test_can_start_a_list_and_retrieve_it_later(self):

        #    def test_can_log_in_to_a_new_account(self):
        #Edith has heard about a coll new online to-do app.
        #She goes to check out its homepage.


        self.browser.get('http://localhost:8000') #go to a homepage



        #assert 'To-Do' in browser.title
        #this code does the same thing with line 5
        #if ! 'Django' in browser.title:
            #throw new AssertionError


        #She notices the page title and header mention to-do list
        #assert 'To-Do' in browser.title #make Django show up on the page

        self.assertIn('To-do',self.browser.title)
        #find the h1 text on the text, got the text and look for To-do word
        #in the text
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-do',header_text)

        #She is invited to endter a to-do item straight away

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        #Shy types "Buy peacock feathers" into a text box
        self.enter_a_new_item('Buy peacock feathers')
        #(Edith's hobby is tying fly-fishing lures)


        #when she hits enter, the page udates, and now the page lists
        # 1. Buy peacock feathers" as an item in a to-do lists


        #table = self.browser.find_element_by_id('id_list_table')
        #rows = table.find_elements_by_tag_name('tr')
    #    self.assertIn('1. Buy peacock feathers', [row.text for row in rows])
    #Now we refractor the above code
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        #There is still a text box inviting her to add aanother item#
        #She enters "Use peacock feathers to make fly"
        #Edith is methodoical


        self.enter_a_new_item('Use peacock feathers to make a fly')

        #The homepage updates again, and now shows both items on her lists

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
    #    self.assertIn('1. Buy peacock feathers', [row.text for row in rows])
    #    self.assertIn('2. Use peacock feathers to make fly', [row.text for row in rows])

        #Edit wonders whether the site will rememver her list. Then she sees

        #That the site has generated a unique URL for her -- there is some explanatory
        #test to that effect

        #she visits that URL - her to do list is still there.

        #Satisfied, she goes back to sleep
        self.fail('Finish the app!')

if __name__== '__main__':
    unittest.main()
