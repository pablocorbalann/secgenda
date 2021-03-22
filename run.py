# This file is part of: github.com/pablocorbalann/secgenda
"""
The run file is the file that actually has to be runned for the Flask server to
start, to run this file use the Python3.6.9+ interpreter, normally installed in 
your system as "python3":

    $ python3 run.py

Please, if you have any issues running this app report an issue to our Github
repositoy: github.com/pablocorbalann/secgenda

This app has created with love by Pablo Corbalán (@pablocorbalann arround the internet)
"""
try:
    from errors import RunError
    import config
except ImportError as e:
    e_code = "001"
    e_message = "Can't import interal modules that are needed"
    try:
        # Maybe the import that failed is the import of the errors, so
        # in that case we can't log it
        e = RunError(e_code, e, e_message)
        e.show()
    except Exception as e:
        print(f"Can't log error {e_code}: {e}")

try:
    import app
except ImportError as e:
    e_code = "002"
    e_message = f"""
We can't run the application module because it can't be imported. 
Remember to run the file from the root directory of secgenda.

    $ python3 run.py

If the problem consists, please report an issue to our GitHub repository.
"""
    e = RunError(e_code, e, e_message)
    e.show()

if __name__ == "__main__":
    app.run(config.DEBUG, config.HOSTNAME, config.PORT, config.SQL_ROUTE)
