"""
Function takes two lists: streets and drivers.
Drivers are pairs of street names.
Function returns a list of distances between the streets each driver has to travel.
The number of streets n satisfies 2 ≤ n ≤ 10⁵. The number of drivers d satisfies 
1 ≤ d ≤ 10⁵. So efficiency is important.
"""
def count_streets(streets, drivers):
    street_indices = {street: index for index, street in enumerate(streets)}
    return [abs(street_indices[driver[1]] - street_indices[driver[0]]) - 1 
            for driver in drivers]