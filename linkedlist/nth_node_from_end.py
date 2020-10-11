from linkedlist import LinkedList


def nth_node(lst:LinkedList, n):
    if lst.is_empty():
        return -1
    end_node = lst.get_head()
    nth_node = lst.get_head()

    count =0
    while count <n:
        if end_node.next_element is None:
            return -1
        end_node = end_node.next_element
        count +=1

    while end_node:
        end_node = end_node.next_element
        nth_node = nth_node.next_element

    if nth_node:
        return nth_node.data

    return -1

lst = LinkedList()
lst.insert_at_head(21)
lst.insert_at_head(14)
lst.insert_at_head(7)
lst.insert_at_head(8)
lst.insert_at_head(12)
lst.insert_at_head(15)
lst.insert_at_head(10)

lst.print_list()

print(nth_node(lst, 4))