import requests
from avasdk.plugins.model import PythonModel

class currency(PythonModel):

    def __init__(self, name="AVA_Currency_Converter"):
        super().__init__(name)
        self.set_commands_list({**PythonModel._commands, **{\
        "convert" : self.convert,
        "._convert_currency": self._convert_currency}})

    # Look for probables currency words used in the message to convert for
    # the correspondant name on the API.
    # then request the rate and returns it times the value asked
    # (this fonction need the message to be treated beofrehand to get the value
    # as a number)
    def _convert_currency(self, base, target, value):
        tmp = target
        api_addr = 'http://api.fixer.io/'
        symbol_dict = {"euro": "EUR",
                        "dollar": "USD",
                        "pound": "GDP",
                        "yen": "JPY",
                        "won":"KRW",
                        "yuan":"CNY"}
        for item in symbol_dict:
            if base == item:
                base = symbol_dict[item]
            if target == item:
                target = symbol_dict[item]
        str_req = api_addr+'latest?base='+base
        req = requests.get(str_req)
        try:
            result = value * req.json()['rates'][target]
            print(str(result) + ' ' + str(tmp))
        except:
            print("Error in request")
        # return (result)


    #example convert 152 euro to dollar
    def convert(self, command):
        s = command.split(' ')
        value = 1 if s[0] == 0 else int(s[0])
        #extract base_currency && target_currency
        # as well as the value asked
        # from the user message
        self._convert_currency(self, s[1], s[3], value)
