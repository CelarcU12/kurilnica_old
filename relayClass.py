class Relay:

    ## klas za relay
    def __init__(self, name="še v pripravi", val="", sn="", date=""):
        self.name = name
        self.val = val 
        self.sn = sn
        self.date = date
        self.toJson = {"name": self.name,
                        "vrednost": self.val,
                        "serijska": self.sn,
                        "cas": self.date}