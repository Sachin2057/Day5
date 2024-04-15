import re
def validate_email(email:str):
    """
    Checks if the given email is valid or not

    Parameters
    ----------
    email : str
        Email to verify

    Returns
    -------
    bool
        True if email is valid, else false
    """
    regular_expression="^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
    if(not re.match(regular_expression,email)):
        return False
    valid_domail=[
        "yahoo.com",
        "gmail.com",
        "outook.com",
        "fusemachines.com"
        ]
    invalid_domian=["yahoop.com"]
    domain=email.split("@")[-1]
    if domain in invalid_domian:
        return False
    if domain not in valid_domail:
        return False
    return True