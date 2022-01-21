class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)

    def length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next
        
        return count

    def insert(self,data, index):
        if (index < 0 or index>=self.length()):
            raise Exception ("Invalid Input")
        
        elif (index == 0):
            self.insert_at_beginning(data)
            return

        else:
            count = 0
            itr = self.head

            while itr:
                if count == index - 1:
                    node = Node(data, itr.next)
                    itr.next = node
                    break
                itr = itr.next
                count += 1
    
    def remove(self,index):
        if (index < 0 or index>=self.length()):
            raise Exception ("Invalid Input")
        
        elif (index == 0):
            self.head = self.head.next
            return

        else:
            count = 0
            itr = self.head

            while itr:
                if count == index - 1:
                    itr.next = itr.next.next
                    break
                
                itr = itr.next
                count += 1
    
    def printll(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            if itr.next:
                llstr += str(itr.data)+'-->'
            else:
                llstr += str(itr.data)
            itr = itr.next
        print(llstr)

ll = linkedlist()
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.insert(43,1)
ll.insert(5,0)
ll.insert_at_beginning(1)
ll.insert_at_end(100)
ll.printll()
ll.remove(2)
ll.printll()