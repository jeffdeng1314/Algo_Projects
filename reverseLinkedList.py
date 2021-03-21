class node:
    next = None
    val = None


def create():
    root = ptr = node()

    for i in range(10):
        ptr.val = i+1
        ptr.next = node()
        ptr = ptr.next
    
    return root


def rev(root):
    if not root:
        return None

    prev, cur, nex = None, root, root

    while cur.next:
        if nex.next:
            nex = nex.next

        cur.next = prev
        prev = cur
        cur = nex
    
    return prev

def main():
    root = rev(create())

    while root:
        print(root.val)
        root = root.next


main()