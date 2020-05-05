class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):
        # looks like a DLL
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.size = 0
        self.storage = [None] * capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
        # found pseudocode for this algorithm on wikipedia

        fnv_offset_basis = 0xcbf29ce484222325
        fnv_prime = 0x100000001b3
        fnv_size = 2**64

        fnv_hash = fnv_offset_basis

        for char in key:
            fnv_hash = (fnv_hash * fnv_prime) % fnv_size
            fnv_hash = fnv_hash ^ ord(char)

        return fnv_hash

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        # also found pseudocode for this algorithm

        djb_hash = 5381

        for char in key:
            djb_hash = ((djb_hash * 33) + ord(char))

        return djb_hash

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
        if self.size == self.capacity:
            self.resize()
        
        index = self.hash_index(key)

        if self.storage[index]:
            self.delete(key)
            self.put(key, value)
        else:
            self.storage[index] = (key, value)
            self.size += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)

        if self.storage[index] is None:
            print('item not found')
        else:    
            self.storage[index] = None
            self.size -= 1

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.storage[index] is None:
            return None
        else:
            # [index][1] because the key value pair is stored as a tuple
            return self.storage[index][1]

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        self.capacity *= 2
        new_storage = [None] * self.capacity

        for item in self.storage:
            if item is not None:
                index = self.hash_index(item[0])
                new_storage[index] = (item[0], item[1])

        self.storage = new_storage

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
