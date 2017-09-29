###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    orders=[]
    current_cow=cows.copy()
    while current_cow.__len__()>0:
        limit_left=limit
        ## current batch stores the result list of lists
        current_batch=[]
        ## while the empty limit is larger than the minimum weight of what is left, add more
        while limit_left>=current_cow[min(current_cow, key=current_cow.get)]:
            ## copy the curent cow to a secondary one
            current_cow_secondary=current_cow.copy()
            ## get the current max cow
            current=max(current_cow_secondary, key=current_cow_secondary.get)
            ## while the current max is larger than what is limit_left, delete the largest, repeat
            while current_cow_secondary[current]>limit_left:
                del current_cow_secondary[current]
                current=max(current_cow_secondary, key=current_cow_secondary.get)
            ## add the current best to the current batch, then delete it
            current_batch+=[current]
            limit_left-=current_cow[current]
            del current_cow[current]
            ## check if the length is 0
            if current_cow.__len__()==0:
                break
            ## append the current batch to the orders
        orders.append(current_batch)
    return orders

# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    ## all_list to store all possible trips
    all_list=[]
    ## get all possible lists
    for partition in get_partitions(cows):
        all_list.append(partition)
    ## while did not find optimal solution
    while True:
        ## get the current shortest_list
        shortest_list = min(all_list, key=len)
        valid=True
        ## for every list in the sub_list,check if the weight is over the limit for any sub list
        for sub_list in shortest_list:
            current_weight=sum([cows[x] for x in sub_list])
            if current_weight>limit:
                valid=False
        ## if not found over limit, then break the while loop
        if valid:
            break
        ## else remove the current shortest_list then redo from beginning.
        else:
            all_list.remove(shortest_list)
    return shortest_list
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))


