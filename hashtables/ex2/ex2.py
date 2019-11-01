#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for trip in tickets:
        # print("TRIP", trip.source)
        hash_table_insert(hashtable, trip.source, trip.destination)
    # print("HASTABLE", hashtable.storage[1].key)
    # for key in hashtable.storage:
    #     print("KEY", key)
    
    current = hash_table_retrieve(hashtable, "NONE")

    for i in range(length):
        route[i] = current
        current = hash_table_retrieve(hashtable, current)

    return route
