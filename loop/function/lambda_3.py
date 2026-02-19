#write a program to convert list that has mixed case countries names into lowercase countries name using lambda

countries_mixed = ["InDiA", "bRAzIL", "united states", "jAPaN", "FRANCE", "gErMaNy", "sOuTh kOrEa", "CaNaDa", "AUSTRALIA", "itaLY"]

countries_lower = list(map(lambda c : c.lower(), countries_mixed))
print(countries_lower)

