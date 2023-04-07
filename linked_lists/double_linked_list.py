
class Node:
    def __init__(self, data):
        self.item = data
        self.pref = None
        self.nref = None


class DoubleLinkedList:

    def __init__(self):
        self.start_node = None
    
    def insert_in_empty_list(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print('List is not empty')
    

    def insert_at_start(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        new_node = Node(data)
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node

    def insert_at_end(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n is not None:
            if n.nref is None:
                break
            n = n.nref
        new_node = Node(data)
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n

    def insert_after_item(self, x, data):
        if self.start_node is None:
            print('The list is empty')
            return
        n = self.start_node
        while n is not None:
            if n.item == x:
                break
            n = n.nref
        if n is None:
            print('Item is not in the list')
            return
        else:
            new_node = Node(data)
            new_node.nref = n.nref
            new_node.pref = n
            if n.nref is not None:
                n.nref.pref = new_node
            n.nref = new_node
    
    def insert_before_item(self, x, data):
        if self.start_node is None:
            print('The list is empty')
            return
        n = self.start_node
        while n is not None:
            if n.item == x:
                break
            n = n.nref
        if n is None:
            print('Item is not in the list')
        else:
            new_node = Node(data)
            new_node.nref = n
            new_node.pref = n.pref
            if n.pref is not None:
                n.pref.nref = new_node
            n.pref = new_node

    def print_list(self):
        if self.start_node is None:
            print('The list is empty')
            return
        n = self.start_node
        while n is not None:
            if n.nref is None:
                print(n.item)
            else:
                print(n.item, ' ', end = '')
            n = n.nref
        
    def reverse_list(self):
        if self.start_node is None:
            print('The list is empty')
            return
        a = self.start_node
        b = a.nref
        a.nref = None
        a.pref = b
        while b is not None:
            b.pref = b.nref
            b.nref = a
            a = b
            b = b.pref
        self.start_node = a

    def find_item(self, x):
        if self.start_node is None:
            print('false')
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    print('true')
                    break
                else:
                    n = n.nref
            if n is None:
                print('false')

    def delete_item(self, x):
        if self.start_node is None:
            print('Nothing to delete')
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                    n = n.nref
            if n is None:
                print('Nothing to delete')
            else:
                if n == self.start_node:
                    if self.start_node.nref is not None:
                        self.start_node = self.start_node.nref
                        self.start_node.pref = None
                    self.start_node = None
                    return
                if n.nref is None:
                    n.pref.nref = None
                else:
                    n.pref.nref = n.nref
                    n.nref.pref = n.pref


if __name__ == '__main__':
    list = DoubleLinkedList()
    n_items = int(input())
    for i in range(n_items):
        DoubleLinkedList.insert_at_start(list, input())
    DoubleLinkedList.print_list(list)
    DoubleLinkedList.reverse_list(list)
    DoubleLinkedList.print_list(list)
    DoubleLinkedList.find_item(list, '4')
    DoubleLinkedList.delete_item(list, '2')
    DoubleLinkedList.print_list(list)





