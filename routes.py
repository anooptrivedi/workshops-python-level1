import random, sys

#example of a tuple
cities = ('san francisco', 'new york', 'miami')

#example of a dictionary
transit = {
    'san francisco': ('miami',),
    'miami': ('new york', 'san francisco',),
    'new york': ('miami',),
}

city = random.choice(cities)

while True:

    print('Your current location is: ', city)
    routes = transit[city]
    print("From here you can go to",', '.join(routes))
    newroute = input('Which city would you like to go? ')

    if(newroute == 'quit'):
        break
    if newroute in routes:
        if (random.randint(1,3) == 1): # very busy season, 1/3rd chance of getting a ticket
            print('It is Thanks giving!, all tickets sold out for this route, contact your travel agent!')
            exit()
        city = newroute
    else:
        print('You cannot go there, Try Again!')
