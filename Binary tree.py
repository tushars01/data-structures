#Binary Tree implementation

class Node:

    """
        This is the class to create single node
        This class has one method called __init__ to
        assign data value to
    """
    
    __slot__ = '_left','_right','_data',
    
    def __init__(self, data):
            
       self._data = data
       self._left = None
       self._right = None

    def printNodeData(self):
        print(self._data)
    

    


class BinarySearchTree:

    data = input("Please enter the value")

    root = Node(data)

    while(True):
        data = input("Do you want to continue")
        root = Node(data)

        if(root == None):
            return None
        else:
            
        

    

##    root = Node(5)
##
##    #print(root._data)
##    root.printNodeData()
##
##    while(True):
##        input_Node = int(input("Enter the value "))
##        root = Node(5)
        

    
