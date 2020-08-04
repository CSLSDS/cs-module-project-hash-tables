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
    A hash table with `capacity` buckets
    that accepts string keys
    """

    def __init__(self, capacity):
        # check if below min capacity; if True, force min capacity
        if capacity < MIN_CAPACITY:
            raise(ValueError(f'capacity must be >= {MIN_CAPACITY}; setting to min ({MIN_CAPACITY}).'))
            self.capacity = MIN_CAPACITY
            self.load_factor = 0.0
        #   else set self.capacity = capacity arg
        else:
            self.capacity = capacity
        self.data = [HashTableEntry(None, None) for _ in range(capacity)]
        self.head = None
        self.load_factor = 0.0
        
    def find(self, value):
        cur = self.head
        
        while cur is not None:
            if cur.value == value:
                return cur
            
            cur = cur.next

            # if we get here, we didn't find it
            return None # let's say so
        
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        """
        return self.capacity


    def get_load_factor(self, value:float):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        if value < self.load_factor and value < 0.2 and self.capacity > MIN_CAPACITY:
            self.resize(max((self.capacity + 1 )//2, MIN_CAPACITY))
        elif value > self.load_factor and value > 0.7:
            self.resize(self.capacity * 2)
        else:
            self.load_factor = value

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
        """
        ix = self.hash_index(key)
        cur = self.data[ix]
        if cur.key == None: # if cur empty
            cur.key = key
            cur.value = value
        else: # collision
            while cur != None:
                if key == cur.key:
                    prior = cur.value
                    cur.value = value
                    return prior
                prev = cur
                cur = cur.next
            # otherwise EOL
            prev.next = HashTableEntry(key, value)
        self.load_factor +=  (1/self.capacity)

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found."""
        ix = self.hash_index(key)
        cur = self.data[ix]
        value = None
        
        if cur.key == key:
            value = cur.value
            if cur.next is None:
                cur.key = None
                cur.value = None
            else:
                self.data[ix] = cur.next
        
        else:
            prev = cur
            cur = cur.next
            
            while cur != None:
                if key == cur.key:
                    value = cur.value
                    prev.next = cur.next
                prev = cur
                cur = cur.next
            
        if value != None:
            self.load_factor -= (1/self.capacity)
        
        return value
    
    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        """
        ix = self.hash_index(key)
        cur = self.data[ix]
        while cur != None:
            if key == cur.key:
                return cur.value
            cur = cur.next
        else:
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        """
        # store original data
        prior = self.data
        for slot in prior:
            cur = slot
            while cur != None and cur.key != None:
                self.put(cur.key, cur.value)
                cur = cur.next

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
