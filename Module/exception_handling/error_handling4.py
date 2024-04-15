import argparse
import logging
logging.basicConfig(filename="error_handling4.log",
                    level=logging.DEBUG, encoding="utf-8")


class InvalidAgeError(Exception):
    def __init__(self):
        self.message = "Invalid Age"
        super().__init__(self.message)


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--age", required=True)
        arg = parser.parse_args()
        age = int(arg.age)
        if(age > 120 or age < 0):
            raise InvalidAgeError
        else:
            logging.debug(f"Age={age}")
    except InvalidAgeError as e:
        logging.error(f"{e}")
    except Exception as e:
        logging.error(f"{e}")
