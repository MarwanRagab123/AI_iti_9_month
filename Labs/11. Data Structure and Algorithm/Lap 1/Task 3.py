from student import Student

class Queue:
    """
    Implements a queue (FIFO) data structure for Student objects.

    Attributes:
    -----------
    items : list
        List of students in the queue.
    max_size : int or None
        Maximum number of students the queue can hold. None means no limit.
    """

    def __init__(self, max_size=None):
        """
        Initializes an empty queue with an optional maximum size.

        Parameters:
        -----------
        max_size : int, optional
            Maximum number of students in the queue. Default is None.
        """
        self.items = []
        self.max_size = max_size

    def enqueue(self, student):
        """
        Adds a student to the end of the queue.

        Parameters:
        -----------
        student : Student
            The student to add to the queue.

        Returns:
        --------
        bool
            True if the student was added, False if the queue is full.
        """
        if self.is_full():
            print("Queue is full!")
            return False
        self.items.append(student)
        return True

    def dequeue(self):
        """
        Removes and returns the student at the front of the queue.

        Returns:
        --------
        Student or None
            The student removed from the front, or None if the queue is empty.
        """
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.items.pop(0)

    def front(self):
        """
        Returns the student at the front without removing it.

        Returns:
        --------
        Student or None
            The student at the front of the queue, or None if the queue is empty.
        """
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
        --------
        bool
            True if the queue is empty, False otherwise.
        """
        return len(self.items) == 0

    def is_full(self):
        """
        Checks if the queue is full.

        Returns:
        --------
        bool
            True if the queue has reached its maximum size, False otherwise.
        """
        if self.max_size is None:
            return False
        return len(self.items) >= self.max_size

    def size(self):
        """
        Returns the number of students currently in the queue.

        Returns:
        --------
        int
            The number of students in the queue.
        """
        return len(self.items)


if __name__ == "__main__":

    student1 = Student(1, "Marwan", [90, 85, 78, 92, 88])
    student2 = Student(2, "Mohamed", [70, 75, 80, 85, 90])
    student3 = Student(3, "Mahmoud", [95, 90, 85, 100, 92])
    student4 = Student(4, "Ahmed", [80, 85, 70, 100, 60])

    queue = Queue(max_size=5)

    queue.enqueue(student1)
    queue.enqueue(student2)
    queue.enqueue(student3)
    queue.enqueue(student4)

    print("Queue size:", queue.size())

    print("Front Student:", queue.front().get_name())

    removed_student = queue.dequeue()
    print("Dequeued Student:", removed_student.get_name())

    print("Queue size after dequeue:", queue.size())

    while not queue.is_empty():
        s = queue.dequeue()
        print("Removing:", s.get_name())
