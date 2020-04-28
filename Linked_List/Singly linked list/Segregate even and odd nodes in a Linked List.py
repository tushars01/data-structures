#######################################################################
#Given a Linked List of integers, write a function to modify the linked
#list such that all even numbers appear before all the odd numbers in
#the modified linked list. Also, keep the order of even and odd numbers
#same.
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
        
    def segregateEvenOdd(self):

        if self.head is None:
            return

        even = odd = self.head

##        while even and odd:
##            if even.data%2 == 0:
##                if odd.data %2!=0:
##                    even.data, odd.data = odd.data, even.data
##                
##
##            else:
##                if odd.data%2!=0:
##                    even.data, odd.data = odd.data, even.data
##            even = even.next
        while even and odd:
            if even.data%2==0 and odd.data%2!=0:
                even.data, odd.data = odd.data, even.data
                odd = odd.next
            elif even.data%2!=0 and odd.data%2==0:
                odd = even
                
            even =even.next
                
                    
            

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
##    llist.push(5)
##    llist.push(9)
##    llist.push(10)
##    llist.push(1)
##    llist.push(359)
##    llist.push(29)
##    llist.push(29)
##    llist.print_list()
##    print()
##    llist.segregateEvenOdd()


##    Input: 17->15->8->12->10->5->4->1->7->6->NULL
##    Output: 8->12->10->4->6->17->15->5->1->7->NULL
    
##    llist.push(6)
##    llist.push(7)
##    llist.push(1)
##    llist.push(4)
##    llist.push(5)
##    llist.push(10)
##    llist.push(12)
##    llist.push(8)
##    llist.push(15)
##    llist.push(17)
##    print()
##    llist.print_list()
##    llist.segregateEvenOdd()
##    print()
##    llist.print_list()



##Input: 8->12->10->5->4->1->6->NULL
##Output: 8->12->10->4->6->5->1->NULL
    
##    llist.push(6)
##    llist.push(1)
##    llist.push(4)
##    llist.push(5)
##    llist.push(10)
##    llist.push(12)
##    llist.push(12)
##    llist.push(8)
##    print()
##    llist.print_list()
##    llist.segregateEvenOdd()
##    print()
##    llist.print_list()

##Input: 8->12->10->NULL
##Output: 8->12->10->NULL

##Input: 1->3->5->7->NULL
##Output: 1->3->5->7->NULL
    
##    llist.push(8)
##    llist.push(12)
##    llist.push(10)
##    llist.push(6)
##    print()
##    llist.print_list()
##    llist.segregateEvenOdd()
##    print()
##    llist.print_list()

##Input: 1->2->3->4->5->NULL
##Output: 1->3->5->2->4->NULL

##    llist.push(5)
##    llist.push(4)
##    llist.push(3)
##    llist.push(2)
##    llist.push(1)
##    print()
##    llist.print_list()
##    llist.segregateEvenOdd()
##    print()
##    llist.print_list()



##Input: 2->1->3->5->6->4->7->NULL
##Output: 2->3->6->7->1->5->4->NULL
    llist.push(7)
    llist.push(4)
    llist.push(6)
    llist.push(5)
    llist.push(3)
    llist.push(1)
    llist.push(2)
    print()
    llist.print_list()
    llist.segregateEvenOdd()
    print()
    llist.print_list()
