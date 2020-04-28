#Intro to DLL
#inserting data into DLL

class Node:

    def __init__(self, data):

        self.data = data
        self.prev = None
        self.next = None

class DLL:

    def __init__(self):
        self.head = None

    def insertionAtFront(self, data):

        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            new_node.next = None
            self.head = new_node
            
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def insertionAtEnd(self, data):

        if self.head is None:
            new_node = Node(data)
            new_node.next = None
            new_node.prev = None
            self.head = new_node
            #return
        else:
            temp = self.head
            #print(temp)
            while temp.next is not None:
                temp = temp.next
                #print (temp.data)

            new_node = Node(data)
            new_node.prev = temp
            new_node.next = None
            temp.next = new_node
    def insertionAfterGivenNode(self, key, data):

        if self.head is None:
            return

        temp = self.head
        while temp:
            if temp.data==key:
                new_node = Node(data)
                new_node.prev = temp
                new_node.next = temp.next
                if temp.next is not None:
                    temp.next.prev = new_node
                temp.next = new_node
            temp = temp.next
    def insertionBeforeGivenNode(self, key, data):

        if self.head is None:
            return

        temp = self.head
        while temp:
            if temp.data == key:
                new_node = Node(data)
                new_node.next = temp
                new_node.prev = temp.prev
                if temp.prev is not None:
                    temp.prev.next = new_node
                else:
                    self.head = new_node
                temp.prev = new_node
            temp = temp.next

    def deleteKey(self, key):
        if self.head is None:
            return

        temp = self.head

        while temp:
            if temp.data == key:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                temp.prev = None
                temp.next = None
            temp = temp.next
    

    def printDLL(self):

        temp = self.head
        while temp:
            print(temp.data, end = ' ')
            temp = temp.next

if __name__ == '__main__':

    dll = DLL()

    #Insertion at end
    dll.insertionAtEnd(1)
    dll.insertionAtEnd(2)
    dll.insertionAtEnd(3)
    dll.insertionAtEnd(4)
    dll.insertionAtEnd(5)
    dll.insertionAtEnd(6)
    dll.printDLL()
    print()

    dll.deleteKey(3)
    dll.deleteKey(2)
    dll.deleteKey(5)
    dll.printDLL()
    print()



    
     
    
    
    
            
            
            
            

        
