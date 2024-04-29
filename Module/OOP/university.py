import logging


logging.basicConfig(filename="university.log",
                    level=logging.INFO, encoding="utf-8")


class University:
    """
    Class for the university
    Attributes:
        Name
        Location
        Department
    """

    def __init__(self, name, location):
        self.__name = name
        self.__location = location
        self.__departments = []

    def set_departments(self, department):
        """
        Add department

        Parameters
        ----------
        department : Depatment
            Object of the department
        """
        self.__departments.append(department)

    def get_info(self):
        """
        Returns name and location

        Returns
        -------
        _type_
            _description_
        """
        return (self.__name, self.__location)

    def display_info(self):
        """
        Information about the university
        """
        logging.info("---University Info---")
        logging.info("Name:%s", self.__name)
        logging.info("Location:%s", self.__location)
        logging.info("The departments in university are:")
        for i in self.__departments:
            logging.info("Department:%s", i.name)


class Departments(University):
    """
    Class for department
    """

    def __init__(self, universityName,
                 location, departmantName, courses: list):
        """
        Initialize properties

        Parameters
        ----------
        universityName : str
            Name of the university
        location : str
            Location of the university
        departmantName : str
            Object of department
        courses : list
            List of courses
        """
        super().__init__(universityName, location)
        self.name = departmantName
        self.location = location
        self.courses = []
        try:
            for i in courses:
                self.courses.append(i)
        except Exception as exception:
            logging.error("Invalid format of list %s", exception)

    def add_course(self, course):
        """
        Add new course

        Parameters
        ----------
        course : str
            Name of course to add
        """
        self.courses.append(course)

    def display_info(self):
        """
        Display university information
        """
        university_name, location = super().get_info()
        logging.info("---Department info---")
        logging.info("University:%s", university_name)
        logging.info("Locaion:%s", location)
        logging.info("Department Name:%s", self.name)
        logging.info("The courses of the deaprtment are:")
        for i in self.courses:
            logging.info(f"{i}")


engineering = Departments(
    "MIT", "Massachusetts",
    "Engineering", ["Computer", "Mechanical"])
engineering.add_course("Eectronics")
appliedScience = Departments(
    "MIT", "Massachusetts",
    "Applied Science", ["Pysics", "Chemistry"])
university = University("MIT", "Massachusetts")
university.set_departments(engineering)
university.set_departments(appliedScience)
university.display_info()
engineering.display_info()
