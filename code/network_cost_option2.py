# -*- coding: utf-8 -*-
def compute_cost(rate_card, dist_verge, dist_road, n_chamber):
    """Computes network cost using Rate Cards, verge distance and road distance.

    Arguments:
        rate_card(str): Rate Card used
        dist_verge(int): Verge distance in meters
        dist_raod(int): road distance in meters
        n_chamber(int): number of chambers
    Returns:
        Prints network cost.

    """
    if rate_card.lower() == "a":
        cabinet = 1000
        trench_verge = 50 * dist_verge
        trench_road = 100 * dist_road
        chamber = 200
        pot = 100
        equation = cabinet + trench_verge + trench_road + chamber * n_chamber + pot
        print 'The network cost is £ {:,.2f}'.format(equation) + ' using Rate Card B'# formatting number to currency
        return
    elif rate_card.lower() == "b":
        cabinet = 1200
        trench_verge = 40 * dist_verge
        trench_road = 80 * dist_road
        chamber = 200
        if dist_verge is not 0:
            pot = 20 * dist_verge
        else:
            pot = 20 * dist_road
        equation = cabinet + trench_verge + trench_road + chamber * n_chamber + pot
        print 'The network cost is £ {:,.2f}'.format(equation) + ' using Rate Card B'
        return
    else:
        print "Rate Card is nor A nor B"


if __name__ == '__main__':
    #compute_cost("a", 10, 0, 1)
    compute_cost("b", 10, 0, 1)
    #compute_cost("f", 10, 0)

