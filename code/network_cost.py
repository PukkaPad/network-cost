# -*- coding: utf-8 -*-
import sys

def d_verge():
    """Returns verge distance entered by user.

    Arguments:
        None.
    Returns:
        verge distance (m).

    """
    while True:
        try:
            dist_verge = float(raw_input ('Please enter verge distance in meters (or zero): '))
            break
        except ValueError:
            print ("Please enter a valid number, or ctrl C to stop")
    return dist_verge

def d_road():
    """Returns road distance entered by user.

    Arguments:
        None.
    Returns:
        road distance (m).

    """
    while True:
        try:
            dist_road = float(raw_input ('Please enter road distance in meters (or zero): '))
            break
        except ValueError:
            print ("Please enter a valid number, or ctrl C to stop")
    return dist_road

def compute_cost():
    """Computes network cost using Rate Cards (A or B) and number of chambers entered by user.
    It calls d_verge and d_road functions.

    Arguments:
        None.
    Returns:
        Prints network cost.

    """

    rate_card = str(raw_input ('Please enter Rate Card: '))
    chamber_quantity = int(raw_input('Please enter how many chambers: '))
    dist_verge = d_verge()
    dist_road = d_road()

    if rate_card.lower() == "a":
        cabinet = 1000
        trench_verge = 50 * dist_verge
        trench_road = 100 * dist_road
        chamber = 200
        pot = 100
        equation = cabinet + trench_verge + trench_road + chamber * chamber_quantity+ pot
        print 'The network costs is £ {:,.2f}'.format(equation) + ' using Rate Card A'  # formatting number to currency
        return
    if rate_card.lower() == "b":
        cabinet = 1200
        trench_verge = 40 * dist_verge
        trench_road = 80 * dist_road
        chamber = 200
        if dist_verge is not 0:
            pot = 20 * dist_verge
        else:
            pot = 20 * dist_road
        equation = cabinet + trench_verge + trench_road + chamber * chamber_quantity + pot
        print ' The network costs is £ {:,.2f}'.format(equation) + ' using Rate Card B'
        return
    else:
        print "Rate Card is nor A nor B"

if __name__ == '__main__':
    try:
        compute_cost()
    except KeyboardInterrupt:
        print('You cancelled the operation.')
        sys.exit(0)

