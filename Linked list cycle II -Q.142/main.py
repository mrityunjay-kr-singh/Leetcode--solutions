# PROBLEM NO. :-142 (Find and return the starting Node of the cycle.)
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

a = Node(3)
b = Node(2)
c = Node(0)
d = Node(-4)

a.next = b
b.next = c
c.next = d
d.next = b

head = a
slow = head
fast = head
pos = 0

while(fast!=None and fast.next!=None):
    fast = fast.next.next
    slow = slow.next
    if(slow == fast):
        slow = head
        while(slow!=fast):
            slow = slow.next
            fast = fast.next
            pos+=1
        break
print(pos)            
        


    