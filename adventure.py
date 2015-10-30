from data import locations, description, items, map

directions = {
    'west': (-1,0),
    'east': (1,0),
    'north': (0,-1),
    'south':(0,1),
}

position = (0,0)


while True:
    location = locations[position]
    description1 = description[position]
    stuff = items[position]
    mapo = map[position]

    print 'you are at the %s' % location
    print '%s' % description1
    print '%s' % mapo

    Choice = raw_input('You find a %s. Do you pick it up? YES/NO\n' % stuff)
    if Choice == 'yes':
        print "You picked up the %s" % stuff
    else:
        print "You leave the %s and keep going" % stuff

    valid_directions = {}
    for k, v in directions.iteritems():
        possible_position = (position[0] + v[0], position[1] + v[1])
        possible_location = locations.get(possible_position)

        if possible_location:
            print 'to the %s is a %s' % (k, possible_location,)
            valid_directions[k] = possible_position


    direction = raw_input('which direction do you want to go?\n')
    new_position = valid_directions.get(direction)
    if new_position:
        position = new_position
    else:
        print "You walked into a fence"



