from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase): #extend unittest

    def setUp(self): #method within class

        self.browser = webdriver.Firefox() #open firefox before any test
        self.browser.implicitly_wait(3) #

    def tearDown(self):

        self.browser.quit() #close the browser after every test

    def test_can_start_a_list_and_retrieve_it_later(self):

        #    def test_can_log_in_to_a_new_account(self):
        #Edith has heard about a coll new online to-do app.
        #She goes to check out its homepage.


        self.browser.get('http://localhost:8000') #go to a homepage

        self.assertIn('To-Do',self.browser.title)

        #assert 'To-Do' in browser.title
        #this code does the same thing with line 5
        #if ! 'Django' in browser.title:
            #throw new AssertionError


        #She notices the page title and header mention to-do list
        #assert 'To-Do' in browser.title #make Django show up on the page

        #She is invited to endter a to-do item straight away
        #Shy types "Buy peacock feathers" into a text box
        #(Edith's hobby is tying fly-fishing lures)

        #when she hits enter, the page udates, and now the page lists
        # 1. Buy peacock feathers" as an item in a to-do lists

        #There is still a text box inviting her to add aanother item#
        #She enters "Use peacock feathers to make fly"
        #Edith is ethological

        #The homepage updates again, and now shows both items on her lists
        #Edit wonders whether the site will rememver her list. Then she sees

        #That the site has generated a unique URL for her -- there is some explanatory
        #test to that effect

        #she visits that URL - her to do list is still there.

        #Satisfied, she goes back to sleep
        self.fail('Finish the app!')
        
if __name__== '__main__':
    unittest.main()
