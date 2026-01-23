#write a program display marriage compatibility for male female using birth dates as per below link,  accept birth day and birth month from user as separate input for both male & female. decide zodiac sign as per previous example and then use zodiac sign to decide  marriage compatibility
#https://miro.medium.com/v2/resize:fit:1100/format:webp/1*f58HMTVzfN2XvCPR23wXgA.jpeg
'''
    Aries: March 21–April 19
    Taurus: April 20–May 20
    Gemini: May 21–June 21
    Cancer: June 22–July 22
    Leo: July 23–August 22
    Virgo: August 23–September 22
    Libra: September 23–October 22
    Scorpio: October 24–November 21
    Sagittarius: November 22–December 21
    Capricorn: December 22–January 19
    Aquarius: January 20–February 18
    Pisces: February 19–March 20
'''
male = None
female = None
day1 = int(input("enter birthdate of male :"))
month1 = int(input("enter birth month of male :"))

day2 = int(input("enter birth date of female :"))
month2 = int(input("entee birth month of female :"))

if (month1 == 3 and day1 >= 21) or (month1 == 4 and day1 <= 19):
    print("aries")
    male = 'aries'

elif (month1 == 4 and day1 >= 20) or (month1 == 5 and day1 <=20):
    print("taurus")
    male = 'taurus'

elif (month1 == 5 and day1 >= 21) or (month1 == 6 and day1 <= 21):
    print("gemini")
    male = 'gemini'

elif (month1 == 6 and day1 >= 22) or (month1 == 7 and day1 <= 22):
    print("cancer")
    male = 'cancer'

elif (month1 == 7 and day1 >= 23) or (month1 == 8 and day1 <= 22):
    print("leo")
    male = 'leo'

elif (month1 == 8 and day1 >= 23) or (month1 == 9 and day1 <= 22):
    print("virgo")
    male = 'virgo'

elif (month1 == 9 and day1 >= 23) or (month1 == 10 and day1 <= 22):
    print("libra")
    male = 'libra' 

elif (month1 == 10 and day1 >= 24) or (month1 == 11 and day1 <= 21):
    print("scorpio")
    male = 'scorpio'

elif (month1 == 11 and day1 >= 22) or (month1 == 12 and day1 <= 21):
    print("Sagittarius")
    male = 'sagittarius'

elif (month1 == 12 and day1 >= 22) or (month1 == 1 and day1 <= 19):
    print("Capri")
    male = 'capri'

elif (month1 == 1 and day1 >= 20) or (month1 == 2 and day1 <= 18):
    print("Aquarius")
    male = 'aquarius'

elif (month1 == 2 and day1 >= 19) or (month1 == 3 and day1 <= 20):
    print("Pisces")
    male = 'pisces'

else:
    print("invlaid data")


if (month2 == 3 and day2 >= 21) or (month2 == 4 and day2 <= 19):
    print("aries")
    female = 'aries'

elif (month2 == 4 and day2 >= 20) or (month2 == 5 and day2 <=20):
    print("taurus")
    female = 'taurus'

elif (month2 == 5 and day2 >= 21) or (month2 == 6 and day2 <= 21):
    print("gemini")
    female = 'gemini'

elif (month2 == 6 and day2 >= 22) or (month2 == 7 and day2 <= 22):
    print("cancer")
    female = 'cancer'

elif (month2 == 7 and day2 >= 23) or (month2 == 8 and day2 <= 22):
    print("leo")
    female = 'leo'

elif (month2 == 8 and day2 >= 23) or (month2 == 9 and day2 <= 22):
    print("virgo")
    female = 'virgo'

elif (month2 == 9 and day2 >= 23) or (month2 == 10 and day2 <= 22):
    print("libra")
    female = 'libra'

elif (month2 == 10 and day2 >= 24) or (month2 == 11 and day2 <= 21):
    print("scorpio")
    female = 'scorpio'

elif (month2 == 11 and day2 >= 22) or (month2 == 12 and day2 <= 21):
    print("Sagittarius")
    female = 'sagittarius'

elif (month2 == 12 and day2 >= 22) or (month2 == 1 and day2 <= 19):
    print("Capri")
    female = 'capri'

elif (month2 == 1 and day2 >= 20) or (month2 == 2 and day2 <= 18):
    print("Aquarius")
    female = 'aquarius'

elif (month2 == 2 and day2 >= 19) or (month2 == 3 and day2 <= 20):
    print("Pisces")
    female = 'pisces'

else:
    print("invlaid data")


if male == 'aries':
    if female in ['taurus','capri','cancer','scorpio']:
        print("Marriage Compatibility : Not Favorable")
    elif female in ['virgo','pisces']:
        print("Marriage Compatibility : good match")
    else:
        print("great match")

elif male == 'leo':
    if female in ['virgo','capri']:
        print("Marriage Compatibility : Not Favorable")
    elif female in ['taurus','aquarius','cancer','scorpio','pisces']:
        print("Marriage Compatibility : good match")
    else:
        print("Marriage Compatibility : great match")

elif male == 'sagittarius':
    if female in ['taurus','virgo','capri']:
        print("Marriage Compatibility : Not Favorable")
    elif female in ['cancer','scorpio','pisces']:
        print("Marriage Compatibility : good match")
    else:
        print("Marriage Compatibility : great match")

elif male == 'taurus':
    if female in ['aries','sagittarius','gemini','aquarius']:
        print("Marriage Compatibility : Not Favorable")
    elif female in ['leo','libra']:
        print("Marriage Compatibility : good match")
    else:
        print("Marriage Compatibility : great match")

elif male == 'virgo':
    if female in ['aries','sagittarius','gemini','libra']:
        print("Marriage Compatibility : Not Favorable")
    elif female in ['leo','aquarius']:
        print("Marriage Compatibility : good match")
    else:
        print("Marriage Compatibility : great match")

elif male == 'capri':
    if female in ['aries','sagittarius','gemini','aquarius']:
        print("Marriage Compatibility : Not Favorable")
    elif female in ['leo','libra']:
        print("Marriage Compatibility : good match")
    else:
        print("Marriage Compatibility : great match")

elif male == 'gemini':
    if female in ['taurus','cancer','scorpio','pisces']:
        print("Marriage Compatibility : Not Favorable")
    elif female in ['sagittarius','capri','virgo']:
        print("Marriage Compatibility : good match")
    else:
        print("Marriage Compatibility : great match")

elif male == 'libra':
    if female in ['virgo','capri','cancer','scorpio']:
        print("Marriage Compatibility : Not Favorable")
    elif female in ['taurus','aries','pisces']:
        print("Marriage Compatibility : good match")
    else:
        print("Marriage Compatibility : great match")

elif male == 'aquarius':
    if female in ['taurus','virgo','capri','cancer']:
        print("Marriage Compatibility : Not Favorable")
    elif female in ['scorpio','pisces']:
        print("Marriage Compatibility : good match")
    else:
        print("Marriage Compatibility : great match")

elif male == 'cancer':
    if female in ['aries','gemini','libra','aquarius']:
        print("Marriage Compatibility : Not Favorable")
    elif female in ['leo','sagittarius']:
        print("Marriage Compatibility : good match")
    else:
        print("Marriage Compatibility : great match")

elif male == 'scorpio':
    if female in ['sagittarius','gemini','libra','aquarius']:
        print("Marriage Compatibility : Not Favorable")
    elif female in ['aries','leo']:
        print("Marriage Compatibility : good match")
    else:
        print("Marriage Compatibility : great match")
    
elif male == 'pisces':
    if female in ['gemini','libra','aquarius']:
        print("Marriage Compatibility : Not Favorable")
    elif female in ['aries','leo','sagittarius']:
        print("Marriage Compatibility : good match")
    else:
        print("Marriage Compatibility : great match")
