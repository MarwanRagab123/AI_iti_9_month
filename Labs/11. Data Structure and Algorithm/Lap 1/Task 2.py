from student import Student

class Node:
    """
    Represents a node in a stack containing a Student object.

    Attributes:
    -----------
    student : Student
        The student stored in the node.
    next : Node or None
        Pointer to the next node in the stack.
    """
    def __init__(self, student):
        """
        Initializes a Node with a given Student.

        Parameters:
        -----------
        student : Student
            The student to store in this node.
        """
        self.student = student
        self.next = None


class Stack:
    """
    Implements a stack (LIFO) data structure using linked nodes.

    Attributes:
    -----------
    top : Node or None
        The top node of the stack.
    _size : int
        The number of elements in the stack.
    """

    def __init__(self):
        """Initializes an empty stack."""
        self.top = None
        self._size = 0

    def push(self, student):
        """
        Pushes a student onto the top of the stack.

        Parameters:
        -----------
        student : Student
            The student to add to the stack.
        """
        new_node = Node(student)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        """
        Removes and returns the student from the top of the stack.

        Returns:
        --------
        Student or None
            The student at the top of the stack, or None if the stack is empty.
        """
        if self.is_empty():
            return None
        popped = self.top.student
        self.top = self.top.next
        self._size -= 1
        return popped

    def peek(self):
        """
        Returns the student at the top of the stack without removing it.

        Returns:
        --------
        Student or None
            The student at the top of the stack, or None if the stack is empty.
        """
        if self.is_empty():
            return None
        return self.top.student

    def is_empty(self):
        """
        Checks whether the stack is empty.

        Returns:
        --------
        bool
            True if the stack is empty, False otherwise.
        """
        return self.top is None

    def size(self):
        """
        Returns the number of students in the stack.

        Returns:
        --------
        int
            The size of the stack.
        """
        return self._size
