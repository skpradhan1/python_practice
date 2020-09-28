from LinkedList import LinkedList


def reverse(lst: LinkedList):

    if lst.is_empty():
        return lst
    curr = lst.get_head()
    prev = None
    while curr:
        nx1 = curr.next_element
        curr.next_element = prev
        prev = curr
        curr = nx1
        lst.head_node = prev
    return lst


lst = LinkedList()

lst.insert_at_head(10)
lst.insert_at_head(9)
lst.insert_at_head(4)
lst.insert_at_head(6)

lst.print_list()
lst1 = reverse(lst)
lst1.print_list()

