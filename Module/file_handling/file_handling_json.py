"""This module adds student info to json file"""
import json
import logging

logging.basicConfig(filename="file_handling_jon.log",
                    level=logging.INFO, encoding="utf-8")


def add_to_json(filename, info):
    """
    Append data to json

    Parameters
    ----------
    filename : str
        File path
    info : dict
        Information to add
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        data.append(info)
        logging.info("File opened")
        logging.debug(data)
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=3)
        logging.info("Data dumped")
        logging.debug(data)
    except FileNotFoundError:
        logging.error("File not found")
    except Exception as e:
        logging.error("%s", e)


add_to_json("json_data.jon",{"name": "Sachin", "age": 15})
    