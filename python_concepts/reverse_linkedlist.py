class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.items = data
        self.next = None

class LinkList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to reverse the linked list
    def reverse_linkedlist(self):
        prev = None
        n = self.head
        while n is not None:
            next = n.next
            n.next = prev
            prev = n
            n = next
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
            print(temp.items)
            temp = temp.next


# Driver program to test above functions
llist = LinkList()

data_list = input('Input the elements in the linked list, separate with space: ').split()
count=0
for data in data_list:
    count += 1
    if count <=100:
        llist.push(int(data))
    else:
        llist

print("Given Linked List")
llist.printList()
llist.reverse_linkedlist()
print("\nReversed Linked List")
llist.printList()