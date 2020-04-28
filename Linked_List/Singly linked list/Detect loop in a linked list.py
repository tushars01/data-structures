#######################################################################
#Given a linked list, check if the linked list has loop or not. Below
#diagram shows a linked list with a loop.
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

    def getMiddle(self):
        len = self.length()
        mid = int(len/2)
        return self.getNth(mid)

    def countKey(self, key):
        count = 0
        temp = self.head
        while temp:
            if temp.data == key:
                count += 1
            temp = temp.next
        return count

    def detectLoop(self):
        s_ptr = self.head
        f_ptr = self.head

        while s_ptr and f_ptr and f_ptr.next:
            s_ptr = s_ptr.next
            f_ptr = f_ptr.next.next
            if s_ptr == f_ptr:
                return True
        
        

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
    llist.push(1)
    llist.push(9)
    llist.push(10)
    llist.push(1)
    llist.push(10)
    llist.push(30)
    llist.push(1)
    llist.print_list()
    llist.head.next.next.next.next = llist.head
    print()
    #llist.getMiddle()
    print(llist.countKey(9))
    
