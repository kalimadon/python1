class node:
    def __init__(self,item):
        self.item = item
        self.next = None
        
node1 = node([1])
node2 = node([2])
node3 = node([3])

node1.next = node2
node2.next = node3

head = node1


while head != None:
    print(head.item)
    if head.next and head.next.item == 2:
        
        
        
        head = head.next.next 
    else:
        head = head.next
    
head = node2

while head != None:
    print(head.item)
    head = head.next