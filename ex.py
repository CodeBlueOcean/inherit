class Node:

    def __init__(self, value):
        
        self.value = value

        self.next = None



class LinkedList:

    def __init__(self):

        self.head = None



    def append(self, value):

        new_node = Node(value)



        if self.head is None:

            self.head = new_node

            print("Head Node created:", self.head.value)

            return



        node = self.head

        while node.next is not None: # move through list until at the end of list so an existing node doesn't get overwritten 

            node = node.next



        node.next = new_node

        print("Appended new Node with value:", node.next.value)



    def prepend(self, value):

        new_node = Node(value)



        if self.head is None:

            self.head = new_node

            print("Head Node created:", self.head.value)

            return



        node = self.head # save the existing head node to generic "node" variable

        self.head = new_node # assign new node as head node

        self.head.next = node # put new head node before existing head node

        print("Prepended new Head Node with value:", self.head.value)

        print("Node following Head is:", self.head.next.value)





llist = LinkedList()

llist.prepend("First Node")

llist.prepend("Inserted New First Node")