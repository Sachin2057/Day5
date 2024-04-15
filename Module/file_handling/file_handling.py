"""This module reads filter data of student with age 18 and above"""
import logging
import pandas as pd


logging.basicConfig(filename="file_handling.log",
                    level=logging.INFO, encoding="utf-8")

try:
    data = pd.read_csv("sachin.csv")
    logging.info("file opened sucessfully")
    above_18 = data[data["Age"] >= 18]
    above_18.to_csv("output.csv", index=False)
    logging.info("Data dumped")
except FileNotFoundError:
    logging.error("File not found")
except Exception as e:
    logging.error("Found exception %s", e)
