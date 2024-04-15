import logging


logging.basicConfig(filename="file_handling_logging.log",
                    level=logging.DEBUG, encoding="utf-8")


def search_log(file, key_word):
    """
    Search for keyword in log
    Parameters
    ----------
    file : str
        Path of file
    key_word : str
        Keyword to search
    """
    result = []
    try:
        with open(file, mode='r', encoding='utf-8') as f:
            data = f.readlines()
            for i in data:
                j = i.split(" ")
                if(key_word in j):
                    result.append(i)
            f.close()
        logging.debug(result)
    except Exception as e:
        logging.error("Error occured %s", e)


search_log("example.log", "should")
