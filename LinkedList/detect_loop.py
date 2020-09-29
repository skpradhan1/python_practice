from LinkedList import LinkedList


def detect_loop(lst:LinkedList):

    if lst.is_empty():
        return False

    slow_p = lst.get_head()
    fast_p = lst.get_head()

    while slow_p and fast_p :
        slow_p = slow_p.next_element
        fast_p = fast_p.next_element.next_element

        if slow_p == fast_p:
            print('loop found')
            return True

    print('no loop found')
    return False

lst = LinkedList()

lst.insert_at_head(21)
lst.insert_at_head(14)
lst.insert_at_head(7)
lst.insert_at_head(9)

flg = detect_loop(lst)

print(flg)