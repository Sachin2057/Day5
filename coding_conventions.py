import json
import logging
import os

logging.basicConfig(
    filename="logs\\coding_conventions.logs", level=logging.INFO)


def add_students(student_id, name,
                 age, grade):
    """
    Function to add student record

    Parameters
    ----------
    student_id : int
        Identity number of student
    name : String
        Name of the student
    age : int
        Age of the student
    grade : float
        Grade of student
    """
    if not os.path.exists("student_record.json"):
        data = []
        with open("student_record.json", 'w', encoding='utf-8') as f:
            data.append({"ID": student_id, "Name": name,
                        "Age": age, "Grade": grade})
            json.dump(data, f, indent=4)
            logging.info("Logging successfull")
    else:
        try:
            with open("student_record.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                print(data)
                print(type(data))
                logging.info("Record opened sucessfully")
                logging.debug(data)
            data.append({"ID": student_id, "Name": name,
                        "Age": age, "Grade": grade})
            print(data)
        except FileNotFoundError:
            print("File not found to open for adding")
        try:
            with open(file="student_record.json", mode="w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
                logging.info("Logging successfull")
        except FileNotFoundError as e:
            print("Error occurend %s", e)
        except Exception as e:
            print("Error occured %s", e)


def search_student(key):
    """
    Search student by name and id

    Parameters
    ----------
    key : int or string
        Key to search the student

    Returns
    -------
    String
        Age and grade of student if found else None
    """
    try:
        with open("student_record.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            logging.info("Record opened sucessfully")
            logging.debug(data)
            f.close()
        if isinstance(key, int):
            for i in data:
                if i["ID"] == key:
                    return f"Age:{i['Age']},Grade:{i['Grade']}"
            logging.info("Student not found")
            return None
        elif isinstance(key, str):
            for i in data:
                if i["Name"] == key:
                    return f"Age:{i['Age']},Grade:{i['Grade']}"
            logging.info("Student not found")
            return None
        else:
            print("Student not found")
            return None
    except Exception as e:
        print(f"Exception occured {e}")


def update_student(key, age=None, grade=None):
    """
    Update_student record

    Parameters
    ----------
    key : string or int
        Name is string_,Id is int
    age : int, optional
        Age to update student, by default None
    grade : float, optional
        Grade to update, by default None
    """
    try:
        with open("student_record.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            logging.info("Record opened sucessfully")
            logging.debug(data)
            f.close()
        if (isinstance(key, int) or isinstance(key, str)):
            if isinstance(key, int):
                for i in data:
                    if i["ID"] == key:
                        if age:
                            i["ID"] = age
                        if grade:
                            i["Grade"] = grade
                logging.info("Student not found")
            elif isinstance(key, str):
                for i in data:
                    if i["ID"] == key:
                        if age:
                            i["Age"] = age
                        if grade:
                            i["Grade"] = grade
                logging.info("Student not found")
            with open(file="student_record.json", mode="w", encoding="utf-8") as f:
                json.dump(data, f)
                logging.info("Update successfull")
                f.close()
        else:
            print("Invalid format")
    except Exception as e:
        print(f"Exception occured {e}")


if __name__ == "main":
    add_students(123, "Sachin", 22, 89.0)
    add_students(124, "Anup", 22, 89.0)
    add_students(154, "Pragyan", 23, 90.0)
    print(search_student(123))
    print(update_student(123, 26, 95.0))
