from errors import DataNotFoundError

def read_and_split(file_route):
    """
    This function is used to read a file and split it's lines into a
    Python list, for example given something like:

        In this dark gray day
        I found you!

    This will return ['In this dark gray day', 'I found you!']

    :param file_route: string -> The file route
    """
    try:
        with open(file_route, "r") as f:
            content = f.read()
            return content.splitlines()
    except FileNotFoundError as e:
        e_code = "008"
        e_message = f"Can't load the data located at {file_route}"
        e = DataNotFoundError(e_code, e, e_message)
        e.show()

def load_logs():
    FILE_ROUTE = "logs.txt"
    return read_and_split(FILE_ROUTE)

def load_logs_codes():
    FILE_ROUTE = "errors.txt"
    return read_and_split(FILE_ROUTE)
