#create module currency.py which has below methods 
#    toDollar which convert given Rupees into Dollar 
#    toEuro  which convert given Rupees into Euro 
#    toPound which convert given Rupees into Pound 
#    ToYen which convert given Rupees into Yen

def todollar(rupees):
    dollar = rupees/92
    return dollar

def toeuro(rupees):
    euro = rupees/106
    return euro

def topound(rupees):
    pound = rupees/124
    return pound

def toyen(rupees):
    yen = rupees/0.60
    return yen