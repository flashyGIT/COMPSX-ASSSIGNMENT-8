class Contact:

class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''

    def __init__(self, name: str, number: str):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"


class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''

    def __init__(self, key: str, value: Contact):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''

    def __init__(self, size: int):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key: str):
        hash_value = 0

        for char in key:
            hash_value += ord(char)

        return hash_value % self.size

    def insert(self, key: str, number: str):
        index = self.hash_function(key)

        contact = Contact(key, number)
        new_node = Node(key, contact)

        # If the index is empty, insert the new node
        if self.data[index] is None:
            self.data[index] = new_node
            return

        # Traverse the linked list
        current = self.data[index]

        while current is not None:

            # Update the number if the contact already exists
            if current.key == key:
                current.value.number = number
                return

            # If this is the last node, add the new node
            if current.next is None:
                current.next = new_node
                return

            current = current.next

    def search(self, key: str):
        index = self.hash_function(key)

        current = self.data[index]

        # Search through the linked list
        while current is not None:
            if current.key == key:
                return current.value

            current = current.next

        return None

    def print_table(self):
        for index in range(self.size):
            print(f"Index {index}:", end=" ")

            current = self.data[index]

            if current is None:
                print("Empty")
            else:
                while current is not None:
                    print(f"- {current.value}", end=" ")
                    current = current.next

                print()


# Test your hash table implementation here.

table = HashTable(10)

# Insert contacts
table.insert("John", "909-876-1234")
table.insert("Rebecca", "111-555-0002")

print("Initial Hash Table:")
table.print_table()

# Search for a contact
contact = table.search("John")
print("\nSearch result:", contact)

# Test collisions
table.insert("Amy", "111-222-3333")
table.insert("May", "222-333-1111")

print("\nAfter inserting Amy and May:")
table.print_table()

# Test duplicate keys (update existing contact)
table.insert("Rebecca", "999-444-9999")

print("\nAfter updating Rebecca:")
table.print_table()

# Test searching for a missing contact
print("\nSearching for Chris:", table.search("Chris"))
""" DESIGN MEMO: CONTACT MANAGEMENT SYSTEM

This project implements a contact management system using a custom-built hash table in Python. The purpose of the project is to demonstrate how hash tables store, organize, and retrieve information efficiently without relying on Python's built-in dictionary.

The system consists of three classes: Contact, Node, and HashTable. The Contact class stores each person's name and phone number. The Node class represents an individual entry in the hash table and contains a key, a Contact object, and a pointer to the next node. The HashTable class manages the underlying array and provides methods for inserting, searching, and displaying contacts.

The hash function calculates an index by adding the Unicode values of each character in a contact's name using the ord() function. It then applies the modulo operator using the table size to ensure the resulting index falls within the array's boundaries.

Separate chaining is used to handle collisions. When two or more names produce the same index, their nodes are connected through a linked list. During insertion, the program checks whether a contact with the same name already exists. If it does, the existing phone number is updated instead of creating a duplicate entry. Otherwise, a new node is added to the linked list.

The search method traverses the linked list at the calculated index and returns the matching Contact object or None if no match exists. The print_table method displays every index and its associated contacts.

Testing includes inserting contacts, handling collisions, updating duplicate names, and searching for nonexistent contacts. Overall, this project demonstrates the importance of hashing, linked lists, and collision resolution in creating efficient data storage systems. """
