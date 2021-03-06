#######################################################################
#Write a function to delete a Linked List
#######################################################################

class Node:

    def __init__(self, data):
        self.next = None
        self.data = data

class LinkedList:

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
        if temp == None:
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
    llist.print_list()
    print()
    llist.deleteList()
            
            
            
