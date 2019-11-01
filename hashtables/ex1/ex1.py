#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    
    # Loop through the list and store each key value pair into a hash table
    for i in range(len(weights)):
        difference = hash_table_retrieve(ht, limit-weights[i])
        if difference is None:
            hash_table_insert(ht, weights[i], i)
        else:
            return (i, difference)
        print("DIFF>>>>>>>>>>>", difference)
        print("HT>>>>>>>>>", ht)
    return None

# {4:0, 6:1, 10:2}
# weights_3 = [4, 6, 10, 15, 16]
#         answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
#         self.assertTrue(answer_3[0] == 3)
#         self.assertTrue(answer_3[1] == 1)


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
