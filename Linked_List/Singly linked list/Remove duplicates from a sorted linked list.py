#######################################################################
#Write a function which takes a list sorted in non-decreasing order
#and deletes any duplicate nodes from the list. The list should only
#be traversed once. For example if the linked list is
#11->11->11->21->43->43->60 then removeDuplicates() should convert
#the list to 11->21->43->60.
#######################################################################

from math import ceil
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
        return False
            
    def createLoop(self, n): 

        if self.length() - n < 0:
            return 'Out of range'
        # LoopNode is the connecting node to 
        # the last node of linked list 
        temp = self.head
        ptr = self.head

        for _ in range(1,n):
            #print(ptr)
            ptr = ptr.next

        while temp.next:
            temp = temp.next
        #print("hjhdkf")
        #print(temp.data)
        temp.next = ptr
        print("________")
        print(temp.data)
        print(ptr.data)
        
    def detectAndCount(self):

         if self.head is None:
             return 0
            
         slow_p = self.head
         fast_p = self.head
         self.flag = 0

         while slow_p and fast_p and fast_p.next and slow_p.next and fast_p.next.next:

             
             #print("Hello")
             if slow_p == fast_p and self.flag!=0:
                 #print("Loop detected")
                 #print(slow_p.data)
                 #print()
                 self.count = 1
                 slow_p = slow_p.next
                 #print(fast_p.data)
                 while slow_p != fast_p:
                     print(slow_p.data)
                     self.count += 1
                     slow_p = slow_p.next
                 #print(self.count)
                 return self.count
             slow_p = slow_p.next
             fast_p = fast_p.next.next
             self.flag = 1
         return 0

    def  checkPalindrome(self):
        length = self.length()
        mid = ceil(length/2)
        second_half_list = []
        first = last =  self.head

        print("mid value " + str(length))
        print(last.data)
        for _ in range(0, mid-1):
            print('-----------')
            
            last = last.next
            print(last.data)
        if length%2==0:
            last = last.next
            
        for _ in range(mid, length ):
            second_half_list.append(last.data)
            print(second_half_list)
            last = last.next
        if length %2 != 0:
            second_half_list.append(last.data)
            
        for _ in range(0, mid):
            print(first.data)
            print(second_half_list[-1])
            if first.data==second_half_list[-1]:
                first = first.next
                second_half_list.pop()

        if second_half_list:
            return False
        else:
            return True
            
    def deleteDuplicate(self):

        if self.head is None:
            return

        first = self.head
        second = self.head.next
        while second:

            if first.data == second.data:
                temp  = second
                second = second.next
                first.next = second
                temp = None
            else:
                first = second
                second = second.next
        

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
##    llist.push(4)
##    llist.push(4)
##    llist.push(3)
##    llist.push(2)
##    llist.push(2)
##    llist.push(2)
##    llist.push(1)
##    llist.push(1)

    llist.push(1)
##    llist.push(1)
##    llist.push(1)
##    llist.push(1)
##    llist.push(1)


    llist.push(1)
    llist.push(3)
    llist.push(3)
    llist.push(3)
    

    llist.print_list()
    print()
    llist.deleteDuplicate()
    print()
    llist.print_list()
    
