#write a program to findout coutries whose area is greater given area. 
# use chatgpt to create dictionaries which country name as key and its' area as value.

country_area = {
    "india": 3287263,
    "china": 9596961,
    "united states": 9833520,
    "russia": 17098246,
    "brazil": 8515767,
    "australia": 7692024,
    "canada": 9984670,
    "argentina": 2780400,
    "kazakhstan": 2724900,
    "algeria": 2381741
}

area = int(input("enter area of country :"))

for no in country_area:
    if country_area[no]>area:
        print(no,' ',country_area[no])