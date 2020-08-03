class DLLNode:  #class node
    def __init__(self, data):  # initialize while program
        self.data = data       # data value from nodes
        self.next = None       # next node
        self.previous = None   # previous node

    def __str__(self):         # sreing represation of node value
        return "DLLNode object: data={}".format(self.data)

class DoublyLinked:             # Doublylinked class

    def __init__(self):
        self.head = None

    def add_node(self, data):
        node = DLLNode(data)    # create node called node

        if self.head is not None:
            node.next = self.head # set head to new node
            self.head.previous = node
        self.head = node

    def is_empty(self):
        return self.head is None

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            else:
                current = current.next
        return None

    def remove(self, data):
        # check if head is pointing to node
        node = self.search(data)
        if node:
            if node.previous and node.next:
                node.previous.next = node.next
                node.next.previous = node.previous
            elif node.previous:
                node.previous.next = None
            elif node.next:
                node.next.previous = None
                self.head = node.next
            else:
                self.head = None
            return 1
        else:
            return -1


    def print(self):
        node = self.head
        while node is not None:
            print(node)
            node = node.next

    #Add a node after a given node.:
    # node as previous, insert
    # a new node data the given node
    '''def add_after(self, previous,data):
        pass
        # 1. check if the given prev_node exists
        if previous is None:
            print("This node doesn't exist in DLL")
            return
        #2. allocate node  & 3. put in the data
        new_node = DoublyLinked(data = data)

        # 4. Make next of new node as next of prev_node
        new_node.next = previous.next

        # 5. Make the next of prev_node as new_node
        previous.next = new_node

        # 6. Make prev_node as previous of new_node
        new_node.prev = previous

        # 7. Change previous of new_node's next node */
        if new_node.next is not None:
            new_node.next.previous = new_node'''
