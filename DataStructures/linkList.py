class Node:
    def __init__(self,data):
        self.items = data
        self.ref = None #next


class Linklist:
    def __init__(self):
        self.start_node = None #head



    def travers(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.items, " ")
                n = n.next

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        else:
            n = self.start_node
            while n is not None:
                n = n.ref
            n.ref = new_node

    def insert_after_item(self, x, data):
        n = self.start_node
        print(n.ref)
        while n is not None:
            if n.item == x:
                break
            n = n.ref
        if n is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List has no elements.")
            return

        if x == self.start_node.item:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
            return

        n = self.start_node
        print(n.ref)
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
            if n.ref is None:
                print("List has no items.")
            else:
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node

# Counting Elements:
    def count_elements(self):
        if self.start_node is None:
            return 0
        else:
            count = 0
            n = self.start_node
            while n is not None:
                count += 1
                n = n.ref
            return count









