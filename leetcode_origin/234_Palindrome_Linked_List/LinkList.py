# Define a Node class
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"ListNode({self.value})"


# Define a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """Add a new node to the end of the linked list."""
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, value):
        """Add a new node at the beginning."""
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        """Delete the first occurrence of a value."""
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        if current.next:
            current.next = current.next.next

    def find(self, value):
        """Find a node with the given value."""
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def display(self):
        """Return a list representation of the linked list."""
        nodes = []
        current = self.head
        while current:
            nodes.append(current.value)
            current = current.next
        return nodes