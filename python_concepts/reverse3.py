class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    # Function to insert a new node at the beginning

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

        # Utility function to print the linked LinkedList

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


# Driver program to test above functions
llist = LinkedList()
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for item in A:
    llist.push(item)

# # Driver program
# llist = LinkedList()
# llist.push(8)
# llist.push(7)
# llist.push(6)
# llist.push(5)
# llist.push(4)
# llist.push(3)
# llist.push(2)
# llist.push(1)


print("Given Linked List")
llist.printList()
llist.reverse()
print("\nReversed Linked List")
llist.printList()