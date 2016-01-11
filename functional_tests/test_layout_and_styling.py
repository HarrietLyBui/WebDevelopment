from .base import TodoFunctionalTest

class LayoutAndStylingTest(TodoFunctionalTest):
    def test_layout_and_styling(self):
        #Edith goes to homepage
        self.browser.set_window_size(1024,768) #set size
        self.browser.get(self.live_server_url)

        #She notices the input box is nicely check_input_box_is_centered
        self.check_input_box_is_centered()

        self.enter_a_new_item('testing')
        self.check_input_box_is_centered()



    def check_input_box_is_centered(self):
        #She notices the input box is nicely center
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + (inputbox.size['width']/2),
            512,
            delta=5

            #rounding error
            #in selenium is easier to do the divide by 2 so we choose this
        )
