from LinkedList import LinkedList
def remove_duplicates(ll):
  temp = ll.head
  prev = None
  nodes = set()
  while(temp):
    if(temp.val in nodes):
      prev.next = temp.next
    else:
      nodes.add(temp.val)
      prev = temp
    temp = temp.next
  return ll


llist = LinkedList()
llist.insert_at_end(1)
llist.insert_at_end(1)
llist.insert_at_end(2)
llist.insert_at_end(3)
llist.insert_at_end(3)
llist.insert_at_end(4)
llist.insert_at_end(5)
llist.insert_at_end(5)
new_head = remove_duplicates(llist)
new_head.printList()