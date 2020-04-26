#######################################################################
#Given a Linked List and a number n, write a function that returns
#the value at the n’th node from the end of the Linked List.
#######################################################################

class Node:

    def __init__(self, data):
        self.next = None
        self.data = data

class LinkedList:
    ''' This is the linked list that has many useful methods
        like push, delete, count, search
                                            '''

    def __init__(self):
        self.head = None


    def push(self, data):

        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            #temp = self.head
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def length(self):
        temp = self.head
        count = 0
        
        while temp:
            count += 1
            temp = temp.next
        return count
    def find(self, key):

        temp = self.head
        while temp:
            if temp.data == key:
                return True
            else:
                temp= temp.next
        return False

    def getNth(self, index):

        temp = self.head
        counter = 0
        while counter < index:
            temp = temp.next
            counter += 1
        if temp:
            return temp.data
        return 'Out of range'

    def getNth_from_end(self, index):
        length_method = self.length()
        new_index = length_method - index
        if new_index < 0:
            return 'Out of range '
        return self.getNth(length_method - index)
        #print(length_method)

    def deleteList(self):

        if self.head is None:
            print("List is empty")
            return

        
        while self.head:
            temp = self.head
            self.head = temp.next
            temp = None
        print("All elements deleted from list ")

    def print_list(self):
        temp = self.head
        if temp is None:
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

    print(llist.getNth_from_end(7))
    
