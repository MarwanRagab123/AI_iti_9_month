from student import Student

class Node:
    """
    Represents a node in a doubly linked list containing a Student.

    Attributes:
    -----------
    student : Student
        The student object stored in the node.
    next : Node or None
        Pointer to the next node in the list.
    previous : Node or None
        Pointer to the previous node in the list.
    """

    def __init__(self, student: Student):
        """
        Initializes a Node with a given Student object.

        Parameters:
        -----------
        student : Student
            The student to store in this node.
        """
        self.student = student
        self.next = None
        self.previous = None

    def __repr__(self):
        """
        Returns a string representation of the node including
        student information and average grade.

        Returns:
        --------
        str
            Formatted string with student's name, ID, grades, and average.
        """
        return (f"Name: {self.student.get_name()}, "
                f"Id: {self.student.get_id()}, "
                f"Grades: {self.student.get_grades()}, "
                f"Average: {self.student.get_average()}")


class DoublyLinkedList:
    """
    Implements a doubly linked list of Student nodes.

    Attributes:
    -----------
    head : Node or None
        The first node in the list.
    tail : Node or None
        The last node in the list.
    """

    def __init__(self):
        """Initializes an empty doubly linked list."""
        self.head = None
        self.tail = None

    @staticmethod
    def _link(first, second):
        """
        Helper method to link two nodes together.

        Parameters:
        -----------
        first : Node or None
            The node that will point to the second node as next.
        second : Node or None
            The node that will point to the first node as previous.
        """
        if first:
            first.next = second
        if second:
            second.previous = first

    def add_student_at_end(self, student: Student):
        """
        Adds a new student at the end of the list.

        Parameters:
        -----------
        student : Student
            The student to add.
        """
        student = Node(student)

        if self.head is None:
            self.head = self.tail = student
        else:
            self._link(self.tail, student)
            self.tail = student

    def add_student_at_beginning(self, student: Student):
        """
        Adds a new student at the beginning of the list.

        Parameters:
        -----------
        student : Student
            The student to add.
        """
        student = Node(student)

        if self.head is None:
            self.head = self.tail = student
        else:
            student.next = self.head
            self.head.previous = student
            self.head = student

    def count_student(self) -> int:
        """
        Counts the number of students in the list.

        Returns:
        --------
        int
            Total number of students in the list.
        """
        count = 0
        curr = self.head

        while curr is not None:
            count += 1
            curr = curr.next

        return count

    def delete_node_by_id(self, student_id: int) -> bool:
        """
        Deletes a node from the list by student ID.

        Parameters:
        -----------
        student_id : int
            ID of the student to delete.

        Returns:
        --------
        bool
            True if deletion was successful, False if student not found.
        """
        curr = self.head

        while curr:
            if curr.student.get_id() == student_id:

                if curr.previous is None:  # Head node
                    self.head = curr.next
                    if self.head:
                        self.head.previous = None

                elif curr.next is None:  # Tail node
                    self.tail = curr.previous
                    if self.tail:
                        self.tail.next = None

                else:  # Middle node
                    curr.previous.next = curr.next
                    curr.next.previous = curr.previous
                return True
            curr = curr.next

        return False

    def search_by_name(self, name: str):
        """
        Searches for a student node by name.

        Parameters:
        -----------
        name : str
            Name of the student to search for.

        Returns:
        --------
        Node or None
            The node containing the student if found, else None.
        """
        curr = self.head

        while curr is not None:
            if curr.student.name == name:
                return curr
            curr = curr.next

    def display_forward(self):
        """
        Displays all students in the list from head to tail.
        """
        curr = self.head

        while curr is not None:
            print(curr)
            curr = curr.next

    def display_backward(self):
        """
        Displays all students in the list from tail to head.
        """
        curr = self.tail

        while curr is not None:
            print(curr)
            curr = curr.previous
