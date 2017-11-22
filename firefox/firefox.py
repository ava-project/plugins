from avasdk.plugins.model import PythonModel
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re

### DEMO VERSION ####

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
browser = webdriver.Firefox()
class firefox(PythonModel):
    """docstring for FirefoxPlugin.

        example commande :

        in AVA prompt :
        firefox open youtube =====> open www.youtube.com
        firefox type foo =====> search foo in youtube
        firefox click Name of one of the videos =====> open the link to this videos
        firefox maximize ====> maximize window

    """
    def __init__(self, name="Firefox"):
        super(firefox, self).__init__(name)
        self.set_commands_list({**PythonModel._commands, **{\
        "open" : self.open, \
        "type" : self.type, \
        "click" : self.click, \
        "maximize" : self.maximize_current_window, \
        "exit" : self.exit, \
        "select" : self.select \
        # ,"copy" : self.copy, \
        # "paste" : self.paste

        }})
        self._current_element = None;

    def list_commands(self, option="") :
        for c in self._commands :
            print(c)

    def __reformat_web_query(self, web_search_query) :
        formatted_query = web_search_query;

        if web_search_query.lower().find(' ') != -1 :
            formatted_query = formatted_query.replace(' ', '+')
            formatted_query = 'http://www.google.com/search?q='+formatted_query

        else :
            if web_search_query.lower().find('www.') == -1 :
                formatted_query = 'www.' + formatted_query
            if web_search_query.lower().find('http://') == -1 :
                formatted_query = 'http://' + formatted_query
            if web_search_query.lower().find('.com') == -1 :
                formatted_query = formatted_query + '.com'

        return formatted_query

    def __validate_user_query_field(self, element_name) :

        if element_name == 'q' :
            return True
        if element_name.lower().find('search') != -1 :
            return True
        return False

    def __locate_element_by_text(self, text) :

        element = None
        try :
            element = browser.find_element_by_xpath("//*[contains(translate(text(), '"+ALPHABET+"', '"+ALPHABET.lower()+"'), '"+text.lower()+"')]")
            print(element)
        except BaseException as e :
            print("Unable to locate element with text '"+text+"' . Error : " + str(e))
        return element


    def maximize_current_window(self, decoy='') :
        browser.maximize_window()

    def exit(self, decoy='') :
        browser.quit()

    def select(self, target_name) :
        pass

    def open(self, query) :
        try :
            # self._browser.get(self.__reformat_web_query(web_search_query))
            browser.get(self.__reformat_web_query(self, query))
            print("opened {0}".format(query))

        except BaseException as e :
            print("Invalid web query : " + str(e))

    def type(self, query) :
        input_element = None;

        try :
            input_element = browser.find_elements_by_tag_name("input")
            for e in input_element :
                if self.__validate_user_query_field(self, e.get_attribute('name')) is True :
                    e.clear()
                    e.send_keys(query)
                    e.submit()
                    break

        except BaseException as e :
            print("Invalid search query : " + str(e))
        print("ok")

    def click(self, element_name) :
        try :
            element = self.__locate_element_by_text(self, element_name)
            if element is not None :
                try :
                    element.click()
                except BaseException as e:
                    print("Invalid action : " + str(e))
        except BaseException as e:
            print("problem locating element " + str(e))
        print("done")

    def select(self, element_name) :
        try :
            element = self.__locate_element_by_text(self, element_name)
            if element is not None :
                element.select()
        except BaseException as e:
            print("Invalid action : " + str(e))
        print("done")

    def play(self, command) :
        w = command.split(' ')
        query = ""
        target = ''
        f = 0;
        for word in w :
            if (word == 'in' or word == 'on' or word == 'with') :
                f = 1;
            elif f is 1 :
                    target = self.__reformat_web_query(word);
                    break
            else :
                query += word + ' ';
        print("query = " + query + " webquery = " + target);
        # self.open(target)
        # while i < 5 :
        #     try : self.type(query)
        #     catch (std::)
