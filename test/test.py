from avasdk.plugins.model import PythonModel

class test(PythonModel):
    """
        test plugin
    """

    def __init__(self, name="test"):
        super(test, self).__init__(name)
        self.set_commands_list({**PythonModel._commands, **{\
        "oneshot" : self.oneshot, \
        "interaction": self.interaction, \
        "crash": self.crash, \
        }})

    def crash(self, command):
        """
        """
        return toto()

    def oneshot(self, command):
        print('### ONESHOT ###')

    def interaction(self, command):
        print(str(self.wait_for_user(self, 'test', 'say anything')).upper())
