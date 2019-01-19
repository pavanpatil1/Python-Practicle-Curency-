class Currency(object):
    rsratio = {"Rs":1,"$":72,"£":90,"€":81}
    dcr="Rs"
    @staticmethod
    def update_dcr():
        ch=int(input("Which Currency do you want default:\n1.Rs\t2.$\t3.E\t4.Y"))
        if ch == 1 :
            Currency.dcr="Rs"        
        elif ch==2:
            Currency.dcr="Rs"        
        elif ch==3:
            Currency.dcr="Rs"        
        elif ch==4:
            Currency.dcr="Rs"        
        else:
            Currency.update_dcr()       
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit
    def __str__(self):
        return str(self.value) + " " + self.unit
    def __add__(self,other):
        if isinstance(other, Currency):
            v = (self.value*Currency.rsratio[self.unit] + other.value*Currency.rsratio[self.unit])*1.0
            return Currency(v/Currency.rsratio[Currency.dcr], Currency.dcr)
        else:
            return other + self
    def __radd__(self,other):
        v = self.value + other
        return Currency(v, Currency.dcr)
    def __sub__(self,other):
        if isinstance(other, Currency):
            v = (self.value*Currency.rsratio[self.unit] - other.value*Currency.rsratio[self.unit])*1.0
            return Currency(v, Currency.dcr)
        else:
            v = self.value - other
            return Currency(v/Currency.rsratio[Currency.dcr], Currency.dcr)
    def __rsub__(self,other):
        v = other - self.value
        return Currency(v, Currency.dcr)
print("The default Currency is Rs")
ch=int(input("Do you want to change the default currency\n1.yes\t2.no"))
if ch==1:
    Currency.update_dcr()    
c1 = Currency(6, "$")
c2 = Currency(50, "Rs")
print (c1+c2)
c1.value=3
c2.value=1
c1.unit="€"
c2.unit="$"
c3=Currency(100,"Rs")
print ((c1+c2)-c3)
c1.value=20
c2.value=5
c1.unit="£"
c2.unit=Currency.dcr
print (c1+c2)