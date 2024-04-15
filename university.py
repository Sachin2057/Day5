import logging

logging.basicConfig(filename="university.log",level=logging.INFO,encoding="utf-8")

class University:
    def __init__(self,name,location):
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
        Display company information
        """
        logging.info("Name, %s" ,self.__name)
        logging.info("Location %s" ,self.__location)
        logging.info("The departments in university are:")
        for i in self.__departments:
            logging.info("Department: %s" ,{i.name})
class Departments(University):
    def __init__(self,university_name,location,departmantName,courses:list):
        super().__init__(university_name,location)
        self.name=departmantName
        self.location=location
        self.courses=[]
        try:
            for i in courses:
                self.courses.append(i)
        except Exception as e:
            logging.error(f"Invalid format of list")
    def add_course(self,course):
        self.courses.append(course)
    def display_info(self):
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
appliedScience=Departments("MIT","Massachusetts","Applied Science",["Pysics","Chemistry"])
university=University("MIT","Massachusetts")
university.set_departments(engineering)
university.set_departments(appliedScience)
university.display_info()
engineering.display_info()
    