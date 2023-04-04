def new_node(value):
    return {
        "value" : value,
        "next" : None
    }
def great_list(n,head):
    for i in range(n):
        value = int(input())
        current = new_node(value)
        if head == None:
            head = current
        else:
            prev["next"] = current
        prev = current
    return head

def print_list():
    current = head
    while current != None:
        print(current["value"], end = '  ')
        current = current["next"]
    print()

#Добавление звена в начало списка
def ins_front(head,value):
    current =  new_node(value)
    prev = head
    head = current
    current["next"] = prev
    return head

# Удаление звена из списка с введенным значением
def del_value(val):
    current = head
    while current["value"] != val:
        if current["next"] == None:
            print("value is not available")
            return
        prev = current
        current = current["next"]
    prev["next"] = current["next"]

head = None
n = int(input())
head = great_list(n, head)
print_list()

del_value(element)
