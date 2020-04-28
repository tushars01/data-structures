##################################################################
#Write a function to delete a given node in a doubly linked list.
##################################################################

class Node:

    def __init__(self,data):
        
        self.data = data
        self.next = None
class LinkedList:

    def __init__(self):
        self.head = None

    #At the front of the linked List
    def insertion_at_front(self, data):

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertion_at_end(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        
    def insertion_after_given_element(self, data, element):

        if self.head is None:
            print("No data found")
            #return

        else:
            temp = self.head

            while temp:
                #print(temp.data)
                if temp.data == data:
                    new_node = Node(element)
                    new_node.next = temp.next
                    temp.next = new_node
                    return
                else:
                    temp = temp.next
                    #return
            

    def printList(self):
        temp = self.head
        #print(temp.data)
        while temp:
            print(temp.data, end=' ')
            
            temp = temp.next
        
        



if __name__ == '__main__':

    llist = LinkedList()
##    llist.insertion_at_front(12)
##    llist.insertion_at_front(120)
##    llist.insertion_at_front(1)
##    llist.insertion_at_front(14)
##    llist.insertion_at_front(57)
##    llist.insertion_at_front(9000)
    #print(llist.printList())

    llist.insertion_at_end(3)
    llist.insertion_at_end(6)
    llist.insertion_at_end(1)
    llist.insertion_at_end(29)
    llist.insertion_at_end(2)
    
    print(llist.printList())

    llist.insertion_after_given_element(1, 1000)
    
    print(llist.printList())

