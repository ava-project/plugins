from avasdk.plugins.model import PythonModel
import wikipedia
import re

class WikiPlugin(PythonModel):

    def __init__(self, name="AVA_Wikipedia"):
        super().__init__(name)
        self.set_commands_list({**PythonModel._commands, **{\
        "who is" : self.ask, \
        "what is": self.ask}})

    # Get the first sentence of the resume on wikipedia,
    # then remove complementary informations comprised between parentheses
    def ask(self, keyword):
        result = wikipedia.summary(keyword, sentences=1)
        epured_result = re.sub("[\(\[].*?[\)\]]", "", result)
        print(result)
        return epured_result

# toto = WikiPlugin()
# toto.ask("barack")
