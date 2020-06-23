import hashlib

class Call: 
    def __init__(self, date, precinct, address, status_code) :
        self.date = date.string 
        self.precinct = precinct.string 
        self.address = address.string.replace("X", "0") + " ST. LOUIS, MO."
        self.status_code = status_code.string
        self.mhash = hashlib.md5()

    def handleNoneType(self, element) :
        result = 'NoneType'
        if element is not None :
            result = element

        return result 

    def getCallDate(self) :
        return self.date

    def getPrecinct(self) :
        return self.precinct

    def getAddress(self) :
        return self.address

    def getStatusCode(self) :
        return self.status_code

    def getHashCode (self) :
        self.mhash.update(self.handleNoneType(self.date).encode('utf-8') + 
            self.handleNoneType(self.precinct).encode('utf-8') + 
            self.handleNoneType(self.address).encode('utf-8') + 
            self.handleNoneType(self.status_code).encode('utf-8'))

        return self.mhash.hexdigest()

    def toString (self) :
        return "\thash code: " + self.getHashCode().ljust(34) + "date: " + self.date.ljust(25) + "precinct: " + self.precinct + "\taddress: " + self.address.ljust(40) + "\tstatus code: " + self.status_code 
