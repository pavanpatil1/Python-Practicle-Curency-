class currency(object):
    pavan = {'rupees':1,'doller':80,'uro':70,'pound':50}   
    def __init__(self,value,unit):
        self.value = value
        self.unit = unit 


    def __str__(self):
        return str(self.value)+str(self.unit)
 
    def __add__(self,other):
        if isinstance(other,currency):
            a = self.value *currency.pavan[self.unit] + other.value *currency.pavan[other.unit]
            v = a/currency.pavan[self.unit]
            u = self.unit
            return currency(v,u)
        else:
            v = self.value + other
            u = self.unit
            return currency(v,u)

    def __radd__(self,other):
        v = self.value + other
        u = self.unit
        return currency(v,u)

    def __sub__(self,other):
        if isinstance(other,currency):
            a = self.value * currency.pavan[self.unit] - other.value * currency.pavan[other.unit]
            v = a/currency.pavan[self.unit]
            u = self.unit
            return currency(v,u)

p = currency(6,'doller') 
d = currency(50,'rupees') 
b = currency(3,'uro')                                     
n = currency(5,'pound')
r = currency(100,'rupees')
t = currency(1,'doller') 


print ""
print "_______________________________________________________________"
print p + d
print ""
print b + t - r
print ""
print 20 +  
n
print "_______________________________________________________________"


