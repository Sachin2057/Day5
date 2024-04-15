"""This module is for logging"""
import logging


logging.basicConfig(filename="university.log",level=logging.INFO,encoding="utf-8")

class University:
    """
    Class to represent university
    """
    def __init__(self,name,location):
        """
        Parameters
        ----------
        name : str
            Name of university
        location : str
            Location of university
        """
        self.__name=name
        self.__location=location
        self.__departments=[]
    def set_departments(self,department):
        """
        Add departments to university

        Parameters
        ----------
        department : Departments
            Object of department to add
        """
        self.__departments.append(department)
    def get_info(self):
        """
        Get university name and location

        Returns
        -------
        (str,str)
            Name and location of university   
        """
        return (self.__name,self.__location)
    def display_info(self):
        """
        Display university information
        """
        logging.info("Name, %s" ,self.__name)
        logging.info("Location %s" ,self.__location)
        logging.info("The departments in university are:")
        for i in self.__departments:
            logging.info("Department: %s" ,{i.name})
class Departments(University):
    """
        Department of university 
        Inherites from University class
    """
    def __init__(self,university_name,location,departmantName,courses:list):
        super().__init__(university_name,location)
        self.name=departmantName
        self.location=location
        self.courses=[]
        try:
            for i in courses:
                self.courses.append(i)
        except Exception as exception:
            logging.error("Invalid format of list %s",exception)
    def add_course(self,course):
        """
        Add new course

        Parameters
        ----------
        course : str
            Course to add
        """
        self.courses.append(course)
    def display_info(self):
        """
        Display department information
        """
        university_name,location=super().get_info()
        logging.info("---Department info---")
        logging.info("University %s" ,university_name)
        logging.info("Locaion:%s" ,location)
        logging.info("Department Name:%s" ,self.name)
        logging.info("The courses of the deaprtment are:")
        for i in self.courses:
            logging.info("%s",i)
engineering=Departments("MIT","Massachusetts","Engineering",["Computer","Mechanical"])
engineering.add_course("Eectronics")
applied_science=Departments("MIT","Massachusetts","Applied Science",["Pysics","Chemistry"])
university=University("MIT","Massachusetts")
university.set_departments(engineering)
university.set_departments(applied_science)
university.display_info()
engineering.display_info()
    