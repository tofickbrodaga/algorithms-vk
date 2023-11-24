from typing import Any

class Node(object):
    def __init__(self, data: list[Any]) -> None:
        self.data = data 
        self.next = None

class LinkedList(object):
    def __init__(self) -> None:
        self.head = None

    def append_front(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def append_back(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
            cur_node.next = new_node
    def print_list(self):
        cur_node = self.head
        output = ""
        while cur_node is not None:
            output += str(cur_node.data)
            if cur_node.next:
                output += " -> "
                cur_node = cur_node.next
