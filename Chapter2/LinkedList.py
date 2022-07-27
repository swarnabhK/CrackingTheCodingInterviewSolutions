from Node import Node
class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self,val):
    new_node = Node(val)
    new_node.next = self.head
    self.head = new_node
  
  def insert_after_node(self,prev_node,val):
    new_node = Node(val)
    new_node.next = prev_node.next
    prev_node.next = new_node
  
  def insert_at_end(self,val):
    new_node = Node(val)
    if(self.head is None):
      self.head = new_node
      return
    temp = self.head
    while(temp.next):
      temp = temp.next
    
    temp.next = new_node
  
  def printList(self):
    temp = self.head
    while(temp):
      print(temp.val,end=' ')
      temp = temp.next

llist = LinkedList()
llist.insert_at_end(6)
llist.insert_at_beginning(7)
llist.insert_at_beginning(1)
llist.insert_at_end(4)
llist.insert_after_node(llist.head.next.next,8)
llist.printList()
