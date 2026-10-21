
# Implementation of Stack and Queue Using Linked Lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(data, "pushed onto stack.")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow: Stack is empty.")
            return

        data = self.top.data
        self.top = self.top.next
        print("Popped element:", data)

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return

        current = self.top
        print("Stack (top to bottom):", end=" ")
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(data, "inserted into queue.")

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow: Queue is empty.")
            return

        data = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        print("Removed element:", data)

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return

        current = self.front
        print("Queue (front to rear):", end=" ")
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()


def read_integer(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return None


def main():
    stack = Stack()
    queue = Queue()

    while True:
        print("\n===== STACK AND QUEUE SYSTEM =====")
        print("1. Push to Stack")
        print("2. Pop from Stack")
        print("3. Display Stack")
        print("4. Enqueue to Queue")
        print("5. Dequeue from Queue")
        print("6. Display Queue")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            value = read_integer("Enter value: ")
            if value is not None:
                stack.push(value)

        elif choice == "2":
            stack.pop()

        elif choice == "3":
            stack.display()

        elif choice == "4":
            value = read_integer("Enter value: ")
            if value is not None:
                queue.enqueue(value)

        elif choice == "5":
            queue.dequeue()

        elif choice == "6":
            queue.display()

        elif choice == "7":
            print("Program terminated.")
            break

        else:
            print("Invalid choice. Please select 1 to 7.")


if __name__ == "__main__":
    main()
