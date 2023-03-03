import sys
input = sys.stdin.readline


class Node():
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DList():
    def __init__(self):
        self.head = Node(data=None)
        self.tail = Node(data=None, prev=self.head)
        self.head.next = self.tail
        self.size = 0
        self.cursor = self.tail

    def append(self, char):
        new_node = Node(data=char, prev=self.cursor.prev, next=self.cursor)
        self.cursor.prev.next = new_node
        self.cursor.prev = new_node
        self.size += 1

    def pop(self):
        if self.cursor.prev != self.head:
            self.cursor.prev.prev.next = self.cursor
            self.cursor.prev = self.cursor.prev.prev
            self.size -= 1

    def cursor_left(self):
        if self.cursor.prev != self.head:
            self.cursor = self.cursor.prev

    def cursor_right(self):
        if self.cursor != self.tail:
            self.cursor = self.cursor.next

    def set_DList(self, string_data):
        for char in string_data:
            self.append(char)

    def read_data(self):
        result = ""
        indicator = self.head.next
        while indicator != self.tail:
            result += indicator.data
            indicator = indicator.next
        return result


string_data = input().rstrip()
M = int(input())
command_list = [tuple(input().rstrip().split()) for _ in range(M)]

d_list = DList()
d_list.set_DList(string_data)

for command in command_list:
    if command[0] == 'L':
        d_list.cursor_left()
    elif command[0] == 'D':
        d_list.cursor_right()
    elif command[0] == 'B':
        d_list.pop()
    else:
        d_list.append(command[1])

print(d_list.read_data())
