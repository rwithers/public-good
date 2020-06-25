import hashlib


class Call: 
    def __init__(self, date, precinct, address, status_code) :
        self.date = date 
        self.precinct = precinct 
        self.address = address.replace("X", "0") + " ST. LOUIS, MO."
        self.status_code = status_code

        self.mhash = hashlib.md5()

    def handleNoneType(self, element) :
        result = 'NoneType'
        if element is not None :
            result = element

        return result 

    def getCallDate(self) :
        return self.formatDate(self.date)

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

    def formatDate (self, date) :
        time_result = ""
        elements = date.split()
        time_elements = elements[1].split(':')
        if not time_elements[0]:
            time_elements[0] = '00'
        if not time_elements[1]:
            time_elements[1] = '00'
        if not time_elements[2]:
            time_elements[2] = '00'
        time_result = elements[0] + ' ' + time_elements[0] + ':' + time_elements[1] + ':' + time_elements[2]
        return time_result

