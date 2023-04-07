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

if __name__ == '__main__':
    list = DoubleLinkedList()
    n_items = int(input())
    for i in range(n_items):
        DoubleLinkedList.insert_at_end(list, input())
    DoubleLinkedList.find_item(list, input())
    
