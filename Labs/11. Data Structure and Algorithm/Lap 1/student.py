class Student:
    """
    A class to represent a student.

    Attributes:
    -----------
    id : int
        The unique identifier for the student.
    name : str
        The name of the student.
    grades : list of float
        A list of 5 grades for the student.

    Methods:
    --------
    set_id(id: int) -> bool
        Sets the student's ID if valid integer is provided.
    set_name(name: str) -> bool
        Sets the student's name if valid string is provided.
    set_grade(grades: list[float]) -> bool
        Sets the student's grades if a list of exactly 5 numeric values is provided.
    get_name() -> str
        Returns the student's name.
    get_id() -> int
        Returns the student's ID.
    get_grades() -> list[float]
        Returns the student's grades.
    get_average() -> float
        Returns the average of the student's grades.
    """

    def __init__(self, id: int, name: str, grades: list[float]):
        """
        Initializes a new Student object with id, name, and grades.

        Parameters:
        -----------
        id : int
            Student ID.
        name : str
            Student's name.
        grades : list of float
            List containing exactly 5 grades.
        """
        self.id = id
        self.name = name
        self.grades = grades

    def set_id(self, id: int):
        """
        Sets the student's ID.

        Parameters:
        -----------
        id : int
            The new ID to assign.

        Returns:
        --------
        bool
            True if ID is valid integer and set successfully, False otherwise.
        """
        if isinstance(id, int):
            self.id = id
            return True
        else:
            return False

    def set_name(self, name: str):
        """
        Sets the student's name.

        Parameters:
        -----------
        name : str
            The new name to assign.

        Returns:
        --------
        bool
            True if name is valid string and set successfully, False otherwise.
        """
        if isinstance(name, str):
            self.name = name
            return True
        else:
            return False

    def set_grade(self, grades: list[float]):
        """
        Sets the student's grades.

        Parameters:
        -----------
        grades : list of float
            List of exactly 5 numeric grades.

        Returns:
        --------
        bool
            True if grades are valid and set successfully, False otherwise.
            Prints error messages if validation fails.
        """
        if len(grades) != 5:
            print("Error! You must Enter Exactly 5 Grades")
            return False

        for grade in grades:
            if not isinstance(grade, (int, float)):
                print("Error: All Grades Must be Numbers")
                return False

        self.grades = grades
        return True

    def get_name(self):
        """
        Returns the student's name.

        Returns:
        --------
        str
            The name of the student.
        """
        return self.name

    def get_id(self):
        """
        Returns the student's ID.

        Returns:
        --------
        int
            The ID of the student.
        """
        return self.id

    def get_grades(self):
        """
        Returns the student's grades.

        Returns:
        --------
        list of float
            The list of grades for the student.
        """
        return self.grades

    def get_average(self):
        """
        Calculates and returns the average of the student's grades.

        Returns:
        --------
        float
            The average grade.

        Raises:
        -------
        ZeroDivisionError
            If there are no grades available.
        """
        if len(self.grades) == 0:
            raise ZeroDivisionError("No Grades Available in List!")
        return sum(self.grades) / len(self.grades)
