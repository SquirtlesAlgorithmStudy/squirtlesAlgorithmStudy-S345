class Node(object):
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DList(object):
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None, self.head)
        self.head.next = self.tail
        self.size = 0
        self.indicating_node = Node(None)
        self.cache_nodes = []

    def listSize(self):
        return self.size

    def is_empty(self):
        if self.size != 0:
            return False
        else:
            return True

    def append(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = Node(None, self.head)
            self.head.next = self.tail
        else:
            tmp = self.tail.prev
            newNode = Node(value, tmp, self.tail)
            tmp.next = newNode
            self.tail.prev = newNode
        self.size += 1

    def set_Dlist(self, n, k):
        for i in range(n):
            self.append(i)
            if i == k:
                self.indicating_node = self.tail.prev

    def go_up(self, step):
        for _ in range(step):
            self.indicating_node = self.indicating_node.prev

    def go_down(self, step):
        for _ in range(step):
            self.indicating_node = self.indicating_node.next

    def delete(self):
        if self.is_empty():
            print("Underflow Error")
            return
        else:
            tmp = self.indicating_node
            self.cache_nodes.append(tmp)
            if tmp == None:
                return
            elif tmp == self.head:
                tmp = self.head
                self.head = self.head.next
                self.head.prev = None
                self.indicating_node = self.head
            else:
                if tmp.next == self.tail:
                    self.indicating_node = tmp.prev
                else:
                    self.indicating_node = tmp.next
                tmp.prev.next = tmp.next
                tmp.next.prev = tmp.prev
            self.size -= 1

    def redo(self):
        reverting_node = self.cache_nodes.pop()
        if self.is_empty():
            self.head = reverting_node
            self.tail = Node(None, self.head)
            self.head.next = self.tail
        else:
            if reverting_node.prev != None:
                reverting_node.prev.next = reverting_node
                reverting_node.next.prev = reverting_node
            else:
                tmp = self.head
                self.head = reverting_node
                tmp.prev = self.head
        self.size += 1

    def get_result(self, n):
        result = ""
        node = self.head
        for i in range(n):
            if node.data == i:
                result += 'O'
                node = node.next
            else:
                result += 'X'
        return result


def solution(n, k, cmds):
    table_list = DList()
    table_list.set_Dlist(n, k)

    for cmd in cmds:
        if cmd[0] == 'U':
            table_list.go_up(int(cmd[2:]))
        elif cmd[0] == 'D':
            table_list.go_down(int(cmd[2:]))
        elif cmd[0] == 'C':
            table_list.delete()
        else:
            table_list.redo()

    return table_list.get_result(n)


cmds = ["U 1", "C", "C", "Z"]
print(solution(5, 1, cmds))
