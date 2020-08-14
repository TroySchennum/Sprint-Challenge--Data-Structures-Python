import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if the value is less than the current node's value 
        if value < self.value:
            # does the current node have a left child?
            if self.left:
                self.left.insert(value)
            # otherwise, it doesn't have a left child
            # we can park the new node here 
            else:
                self.left = BSTNode(value)
        # otherwise the value is greater or equal to the current node's value 
        else:
            # does the current node have a right child?
            if self.right:
                # if it does, call the right child's `insert` method to repeat the process
                self.right.insert(value)
            # otherwise, it doesn't have a right child 
            # we can park the new node here 
            else:
                self.right = BSTNode(value)
    def contains(self, target):
        # base case: check self's value to see if it matches the target's 
        if self.value == target:
            duplicates.append(target)
        # otherwise, we need to go either left or right 
        # compare the target against self's value 
        if target < self.value:
            # base case: if there's no node here, then the target is not in the tree
            if not self.left:
                return False
            # otherwise, there is a node there
            else:
                # call `contains` on the left child
               return self.left.contains(target) 
        else:
            # base case: if there's no node here, then the target is not in the tree
            if not self.right:
                return False
            # otherwise there's a node there 
            else:
                # call `contains` on the right child 
                return self.right.contains(target)
                
for i in names_1 and names_2:
    bst = BSTNode("troy")
    bst.insert(i)
    bst.contains(i)


# for i in bst:
#     if i == i:
#         duplicates.append(i)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
