class Temp:

    ## Temperaturni senzor z imenom, vrednostjo, serijsko številko in časom izmerjene vredenosti
    def __init__(self, name, val, sn, date):
        self.name = name
        self.val = val 
        self.sn = sn
        self.date = date
        self.toJson = {"name": self.name,
                        "vrednost": self.val,
                        "serijska": self.sn,
                        "cas": self.date}
