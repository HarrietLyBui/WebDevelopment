from selenium import webdriver
from .base import TodoFunctionalTest

class NewVisitorTest(TodoFunctionalTest):
    #Now we refractor the above code
    def test_can_start_a_list_and_retrieve_it_later(self):
        #    def test_can_log_in_to_a_new_account(self):
        #Edith has heard about a coll new online to-do app.
        #She goes to check out its homepage.
        self.browser.get(self.live_server_url) #go to a homepage

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


        #when she hits enter, she is taken to a new URL
        #, and now the page lists
        # 1. Buy peacock feathers" as an item in a to-do lists

        edith_list_url = self.browser.current_url
        self.assertRegexpMatches(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        #table = self.browser.find_element_by_id('id_list_table')
        #rows = table.find_elements_by_tag_name('tr')
        #    self.assertIn('1. Buy peacock feathers', [row.text for row in rows])
        #Now we refractor the above code
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

        #Now a new user, Francis, comes along

        #We use a new browser session to make sure no information
        #of Edith's comesalong (EG cookies, local storage)

        self.browser.quit()
        self.browser = webdriver.Firefox()

        #Francis visits the home page. There is no sign of Edith's list

        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        #Francis starts a new list by entering a new item.
        #He is less interesting than Edith
        self.enter_a_new_item('Buy milk')

        #Francis gets his own URL
        francis_list_url = self.browser.current_url
        self.assertRegexpMatches(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        #There is still no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        #Statisfy they both go to sleep

        #Edit wonders whether the site will rememver her list. Then she sees

        #That the site has generated a unique URL for her -- there is some explanatory
        #test to that effect

        #she visits that URL - her to do list is still there.

        #Satisfied, she goes back to sleep
        # self.fail('Finish the app!')
