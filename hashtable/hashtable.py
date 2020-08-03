class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # check if below min capacity; if True, force min capacity
        if capacity < MIN_CAPACITY:
            raise(ValueError(f'capacity must be >= {MIN_CAPACITY}; setting to min ({MIN_CAPACITY}).'))
            self.capacity = MIN_CAPACITY
        #   else set self.capacity = capacity arg
        else:
            self.capacity = capacity
        self.data = [None] * self.capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.data) # capacity?


    def get_load_factor(self, value:float):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        pass

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # key_codes = key.encode()

        # FNV_PRIME = 1099511628211
        # hash = 14695981039346656037
        # maxint = 2 ** 32
        # for x in key:
        #     temp = hash ** ord(x)
        #     hash = (hash * FNV_PRIME) % maxint

        #return hash & 0xffffffffffffffff
        pass

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381

        for st in key:
            hash = (((hash << 5) + hash) + ord(st))

        return hash & 0xffffffff  # return 32 bit version

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        ix = self.hash_index(key)
        self.data[ix] = value


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        delete_ix = self.hash_index(key)

        self.data[delete_ix] = None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        ix = self.hash_index(key)
        hash_entry = self.data[ix]
        if hash_entry != None:
            return self.data[ix]
        else:
            return None


    # def resize(self, new_capacity):
    #     """
    #     Changes the capacity of the hash table and
    #     rehashes all key/value pairs.

    #     Implement this.
    #     """
    #     self.capacity *=2

    #     prior_table = self.table_copy()

    #     self.table = [None] * self.capacity

    #     for i in range(len(prior_table)):
    #         prior_hash = prior_table[i]
    #         while prior_hash:
    #             self.put(prior_hash.key, prior_hash.value)


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    #old_capacity = ht.get_num_slots()
    #ht.resize(ht.capacity * 2)
    #new_capacity = ht.get_num_slots()

    #print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    print("")
