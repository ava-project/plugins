from avasdk.plugins.model import PythonModel
import requests

class CurrencyConverter(PythonModel):

    def __init__(self, name="AVA_Currency_Converter"):
        super().__init__(name)
        self.set_commands_list({**PythonModel._commands, **{\
        "convert" : self.entry_point}})
        self.api_addr = 'http://api.fixer.io/'
        self.symbol_dict = {"euro": "EUR",
                            "dollar": "USD",
                            "pound": "GDP",
                            "yen": "JPY",
                            "won":"KRW",
                            "yuan":"CNY"}

    # Look for probables currency words used in the message to convert for
    # the correspondant name on the API.
    # then request the rate and returns it times the value asked
    # (this fonction need the message to be treated beofrehand to get the value
    # as a number)
    def convert(self, base, target, base_value=1):
        for item in self.symbol_dict:
            if base == item:
                base = self.symbol_dict[item]
            if target == item:
                target = self.symbol_dict[item]
        str_req = self.api_addr+'latest?base='+base
        req = requests.get(str_req)
        try:
            result = base_value * req.json()['rates'][target]
        except:
            return("Error in request")
        return (result)

    #example convert 152 euro to dollar
    def entry_point(self, base_message):
        s = base_message.split(' ')
        value = (s[0]) == 0 ? 1 : int(s[0])
        #extract base_currency && target_currency
        # as well as the value asked
        # from the user message
        return self.convert(s[1], s[2], value)
