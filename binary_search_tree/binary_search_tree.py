import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        
        # if there is NO current node
        # if value is less go left
        if value < self.value and self.left is None:
            self.left = BinarySearchTree(value)
            return
        # else if value is greater than or equal go right
        elif value >= self.value and self.right is None:
            self.right = BinarySearchTree(value)
            return

        # compare to current node
        # if smaller go left and recurse
        if value < self.value:
            self.left.insert(value)
        # if larger or equal go right and recurse
        else:
            self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # compare to the current node value
        if target == self.value:
            return True

        # if smaller, go left
        if target < self.value:
            # if hits end and value not found return False
            if self.left is None:
                return False
            # otherwise recurse and look left
            return self.left.contains(target)

        # if bigger, go right
        if target > self.value:
            # if hits end and value not found return False
            if self.right is None:
                return False
            # otherwise recurse and look right
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # look right until as far right as you can go, this should be the max
        if self.right is None:
            return self.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # go left first
        if self.left is not None:
            self.left.for_each(cb)

        # print the value if you can't go left anymore
        cb(self.value)

        # go right
        if self.right is not None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # for_each is already in order, print        
        self.for_each(print)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create a queue for nodes
        queue = []
        # add current node to queue
        queue.append(node)

        while (len(queue)):
            # get current node
            cur_node = queue[-1]
            # dequeue a node
            queue.pop()

            # print the node
            print(cur_node.value)

            # add its children
            if cur_node.right is not None:
                queue.append(cur_node.right)
            if cur_node.left is not None:
                queue.append(cur_node.left)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create a node_stack
        node_stack = []
        # create a list for visited nodes
        visited = []
        # push the current node onto stack
        node_stack.append(node)

        while (len(node_stack)):
            # print the current value and pop it off
            cur_node = node_stack.pop()

            # check if current node already printed
            if cur_node not in visited:
                # add node to visited list
                visited.append(cur_node)
                # print the node
                print(cur_node.value)
                
                # push the left value of current node if we can
                max_left = cur_node
                while max_left.left is not None:
                    max_left = max_left.left
                    node_stack.append(max_left)

                # push the right value of the current node if we can
                max_right = cur_node
                while max_right.right is not None:
                    max_right = max_right.right
                    node_stack.append(max_right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


# Test Output
testOutput = BinarySearchTree(1)
testOutput.insert(8)
testOutput.insert(5)
testOutput.insert(7)
testOutput.insert(6)
testOutput.insert(3)
testOutput.insert(4)
testOutput.insert(2)

# testOutput.in_order_print(testOutput)
testOutput.bft_print(testOutput)
# testOutput.dft_print(testOutput)
