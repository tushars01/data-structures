#Linked List | Set 3 (Deleting a node)

#Problem statement
#######################################################################
#Given a ‘key’, delete the first occurrence of this key in linked list.
#######################################################################

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self,data):
        
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            new_node = Node(data)
            temp.next = new_node
            
    def delete(self, key):

        temp = self.head
        prev = self.head
        self.is_key_found = False

        if self.head.data == key:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.is_key_found = True
        else:
            
            while temp:

                if temp.data == key:
                    prev.next = temp.next
                    temp = None
                    self.is_key_found = True
                    return
                    
                else:
                    prev = temp
                    temp = temp.next
        
        if self.is_key_found:
            print(str(key) + ' deleted ')
        else:
            print(str(key) + ' not found ')

    def printList(self):
        temp = self.head
        if self.head is None:
            print("No element in the list")
        else:
            
            while temp:
                print(temp.data, end=' ')
                temp = temp.next

if __name__ == '__main__':

    llist = LinkedList()
    llist.append(2)
    llist.append(10)
    llist.append(3)
    llist.append(50)
    llist.append(100)
    llist.append(9)

    llist.printList()
    print()
    llist.delete(2)
    print()
    llist.printList()

    llist.delete(9)
    print()
    llist.printList()

    llist.delete(100)
    print()
    llist.printList()

    llist.delete(3)
    print()
    llist.printList()

    llist.delete(10)
    print()
    llist.printList()

    llist.delete(50)
    print()
    llist.printList()
        
