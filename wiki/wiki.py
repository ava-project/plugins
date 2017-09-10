import re
import wikipedia
from avasdk.plugins.model import PythonModel

class wiki(PythonModel):

    def __init__(self, name="AVA_Wikipedia"):
        super(wiki, self).__init__(name)
        self.set_commands_list({**PythonModel._commands, **{\
        "who" : self.who, \
        "what": self.what}})

    def _ask(keyword):
        result = wikipedia.summary(keyword, sentences=1)
        epured_result = re.sub("[\(\[].*?[\)\]]", "", result)
        print(epured_result)

    def who(self, keyword):
        self._ask(keyword)

    def what(self, keyword):
        self._ask(keyword)
