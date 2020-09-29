from LinkedList import LinkedList


def find_middle_node(lst:LinkedList):
    if lst.is_empty():
        return 0
    length = lst.length()
    mid_node = length//2 if length %2 ==0 else length//2+1
    node = lst.get_head()
    for i in range(mid_node-1):
        node = node.next_element
    return node.data

lst = LinkedList()
lst.insert_at_head(22)
lst.insert_at_head(21)
lst.insert_at_head(10)
lst.insert_at_head(14)
lst.insert_at_head(7)

lst.print_list()
print(find_middle_node(lst))
