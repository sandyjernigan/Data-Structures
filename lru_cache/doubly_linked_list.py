"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    """Our doubly-linked list class. It holds references to the list's head and tail nodes."""

    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):
        if self.head is None and self.tail is None: 
            return "empty"
        curr_node = self.head
        output = ''
        output += f'( {curr_node.value} )'
        while curr_node.next is not None:
            curr_node = curr_node.next 
            output += f' <-> ( {curr_node.value} )'
        return output

    def add_to_head(self, value):
        """Inserts new node as the new head of the list."""
        # adding to an empty list
        new_node = ListNode(value)   
        self.length += 1
        if self.head is None and self.tail is None:
            # create a new node
            self.head = new_node
            self.tail = new_node
        else:
            # adding a new value, to existing list
            # link new_node with current head
            new_node.next = self.head
            self.head.prev = new_node
            # update head
            self.head = new_node
        
    def remove_from_head(self):
        """Removes the List's current head node, making the
        current head's next node the new head of the List.
        Returns the value of the removed Node."""

        # if list is empty
        if self.head is None and self.tail is None:
            return  
        # if list has only one element
        elif self.head == self.tail:
            # unlink the node
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            # we have more than one element
            value = self.head.value
            next_head = self.head.next
            next_head.prev = None
            self.head.next = None
            self.head = next_head
            self.length -= 1
            return value

    def add_to_tail(self, value):
        """Inserts new node as the new tail of the list."""

        # adding to an empty list
        new_node = ListNode(value)   
        self.length += 1
        if self.head is None and self.tail is None:
            # create a new node
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_tail(self):
        """Removes the List's current tail node, Returns the value of the removed Node."""

       # if list is empty
        if self.head is None and self.tail is None:
            return  
        # if list has only one element
        elif self.head == self.tail:
            # unlink the node
            value = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            # we have more than one element
            value = self.tail.value
            prev_tail = self.tail.prev
            prev_tail.next = None
            self.tail.prev = None
            self.tail = prev_tail
            self.length -= 1
            return value

    def move_to_front(self, node):
        """Removes the input node from its current spot in the 
        List and inserts it as the new head node of the List."""
        
        # if node is already in most recent, just return value
        if node is self.head: return node

        # Remove Node by resetting connections around Node
        if node.next: node.next.prev = node.prev
        if node.prev: node.prev.next = node.next

        # If Node is the tail, set a new tail
        if node is self.tail:
            self.tail = self.tail.prev

        # Update head node
        self.head.prev = node
        node.next = self.head
        node.prev = None
        self.head = node

        # Return the Node
        return node

    def move_to_end(self, node):
        """Removes the input node from its current spot in the 
        List and inserts it as the new tail node of the List."""
        
        # if node is already in most recent, just return value
        if node is self.tail: return node

        # Remove Node by resetting connections around Node
        if node.next: node.next.prev = node.prev
        if node.prev: node.prev.next = node.next

        # If Node is the head, set a new head
        if node is self.head:
            self.head = self.head.next

        # Update tail node
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node

        # Return the Node
        return node

    def delete(self, node):
        """Removes a node from the list and handles cases where
        the node was the head or the tail"""

        # If Node is the head, set a new head
        if node is self.head:
            self.head = self.head.next
        
        # If Node is the tail, set a new tail
        if node is self.tail:
            self.tail = self.tail.prev

        # Remove Node by resetting connections around Node
        if node.next: node.next.prev = node.prev
        if node.prev: node.prev.next = node.next

        # Node is removed once there are no more references to the Node
        
    def get_max(self):
        """Returns the highest value currently in the list"""

        curr_node = self.head
        max_value = self.head.value

        if (self.head == None):
            return "empty"
        
        while curr_node.next is not None:
            curr_node = curr_node.next
            
            if(max_value < curr_node.value):
                max_value = curr_node.value

        return max_value

# Testing Output
our_dll = DoublyLinkedList()

[our_dll.add_to_tail(i) for i in [1,2,3,4,5,6,7,8,9]]

print("DLL: ")
print(our_dll)

