class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
 
# instantiate the nodes
node1 = ListNode("The")
node2 = ListNode("boy")
node3 = ListNode("is")
node4 = ListNode("tall")
 
# link the nodes
node1.next = node2
node2.next = node3
node3.next = node4

print("try:",node1.val)
print("try:",node1.next.val)
 
# traverse the linked list and print each node's value
current_node = node1
while current_node is not None:
    print(current_node.val)
    current_node = current_node.next
 
# The
# boy
# is
# tall