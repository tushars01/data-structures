
#######################################################################
#Given a singly linked list and a position, delete a linked list node
#at the given position.
#######################################################################


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            #print(str(data) + ' is the first element' )
        else:
            new_node = Node(data)
            new_node.next = self.head
            #self.head.next = None
            self.head = new_node
        
    def delete(self, position):

    

        if self.head is None:
            print('No element found ')
            return
        elif position == 0:
            temp = self.head
            self.head = temp.next
            temp = None
        else:
            count = 0
            temp = self.head
            prev = self.head
            while count < position:
                prev = temp
                temp = temp.next
                count += 1
            
            if temp is not None:
                
                prev.next = temp.next
                temp.next = None
                print(str(temp.data) + ' Element deleted')
            else:
                print('Out of range exception')

            
                
                
            
                
                

    def print_list(self):
        temp = self.head
        if temp == None:
            print("No element in the list ")
            return

        while temp:
            print(temp.data, end = ' ' )
            temp = temp.next
if __name__ == '__main__':

    llist = LinkedList()
    llist.push(5)
    llist.push(9)
    llist.push(10)
    llist.push(1)
    llist.push(359)
    llist.push(29)

    llist.print_list()
    print()
    llist.delete(6)
    print()
    llist.print_list()
