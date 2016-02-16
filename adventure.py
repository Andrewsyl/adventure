from data import locations, description, items, map

directions = {
    'west': (-1,0),
    'east': (1,0),
    'north': (0,-1),
    'south':(0,1),
}

position = (0,0)

inventory = []

while True:
    location = locations[position]
    description1 = description[position]
    stuff = items[position]
    mapo = map[position]

    print 'you are at the %s' % location
    print '%s' % description1
    print '%s' % mapo

    Choice = raw_input('You find a %s. Do you pick it up? YES/NO\n' % stuff).upper()
    if Choice == 'YES':
        if stuff in inventory:
            print "You aleady have one of those"
            continue
        else:
            print "You picked up the %s" % stuff
            inventory.append(stuff)
    # elif stuff in inventory:
    #     print "You already have one of those"
    #     continue
    elif Choice == "DROP ITEM":
        i = raw_input("which item?: ")
        for j in inventory:
            if j == i:
                inventory.remove(i)
        print "You dropped %s" % i
    else:
        print "You leave the %s and keep going" % stuff

    valid_directions = {}
    for k, v in directions.iteritems():
        possible_position = (position[0] + v[0], position[1] + v[1])
        possible_location = locations.get(possible_position)

        if possible_location:
            print 'to the %s is a %s' % (k, possible_location,)
            valid_directions[k] = possible_position
    print "Inventory: %s" % inventory

    direction = raw_input('which direction do you want to go?\n')
    new_position = valid_directions.get(direction)
    if new_position:
        position = new_position
    else:
        print "You walked into a fence"

print inventory
print "You collected all the items, well done!"


