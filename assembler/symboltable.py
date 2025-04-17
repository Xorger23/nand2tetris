class SymbolTable:
    def __init__(self):
        self.table = {"SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
            "SCREEN": 16384, "KBD": 24576, "R0": 0, "R1": 1, "R2": 2, "R3": 3,
            "R4": 4, "R5": 5, "R6": 6, "R7": 7, "R8": 8, "R9": 9, "R10": 10,
            "R11": 11, "R12": 12, "R13": 13, "R14": 14, "R15": 15}
        self.curaddress = 16

    def create_entry(self, symbol, address):
        self.table[symbol] = address

    def contains(self, symbol):
        return symbol in self.table

    def add(self, symbol, address):
        if self.contains(symbol):
            pass
        else:
            if address == None:
                address = self.curaddress
                self.curaddress += 1
            self.create_entry(symbol, address)

        return self.table[symbol]

    def get_value(self, symbol):
        return self.table[symbol]

    def get_table(self):
        return self.table
