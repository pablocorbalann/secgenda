# This file is part of: github.com/pablocorbalann/secgenda
"""
The errors module contains all the classes that are related to the errors of the application.

There is a class :class Error: that is the parent class for the rest of the errors, from
where all the errors inherit.

More information at our github repository
"""
class Error(BaseException):
    """
    This class is the parent class for all the errors, inherits from the Python
    BaseException class.
    """
    def __init__(self, e_code, e=None, e_message=""):
        """
        This is the constructor method for all the errors, it uses three parameters
        for setting up the error and then raising it.

        :param e_code: int -> The error code (check errors.txt)
        :param e: Exception -> The exception that the error raised
        :param e_message: str -> A custom error message
        """
        self.e_code = e_code
        self.e = e
        self.e_message = e_message
    
    def __repr__(self):
        return f"[E {self.e_code}]: {self.e_message} - {self.e if self.e is not None else ''}"

    def display(self):
        """
        This method is used to display a representation of the error in
        the system console, mainly for development purposes
        """
        print(f"\033[1m\033[91m{self.__repr__()}\033[0m")
    
    def log(self):
        """
        This method is used for loging the error inside the logs file
        from the moment the route of the file is declarated locally,
        we will try to modularize that in the next versions
        """
        ROUTE = "logs.txt"
        try:
            with open(ROUTE, "a") as f:
                f.write("\n" + self.e_code)
        except FileNotFoundError as e:
            e_code = "003"
            e = LogError(e_code, e, f"Can't find the logs route {ROUTE}")
            e.display()
        except Exception as e:
            e = Error("000", e)
            e.display()

    def show(self):
        """
        This method is used for displaying the error in the console and at
        the same time log it in the text file.
        """
        self.display()
        self.log()


class RunError(Error):
    def __init__(self, e_code, e=None, e_message=""):
        super().__init__(e_code, e, e_message)
