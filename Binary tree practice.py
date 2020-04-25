# implementing Binary tree using list

list = [1,4,5,3,6,8,5]




class Node:
    
    __slots__ = '_data', '_left', '_right'

    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None
    
    

    

if __name__ == '__main__':

    node = Node(1)
    node._left = Node(2)
    node._left._left = Node(4)
    node._left._right = Node(5)
    node._right = Node(3)
    #print_preorder_binary_tree(node)
    def print_preorder_binary_tree(node):
        if node:
            
            print(node._data ),
            print_preorder_binary_tree(node._left)
            print_preorder_binary_tree(node._right)

    def print_inorder_binary_tree(node):
        if node:
            print_inorder_binary_tree(node._left)
            print(node._data)
            print_inorder_binary_tree(node._right)

    def print_postorder_binary_tree(node):
        if node:
            print_postorder_binary_tree(node._left)
            print_postorder_binary_tree(node._right)
            print(node._data)
            
            

    print("preorder traversal ")
    print_preorder_binary_tree(node)
    print("inorder traversal ")
    print_inorder_binary_tree(node)
    print("postorder traversal ")
    print_postorder_binary_tree(node)
    

    
        

    

        

    
        
