# This file is part of github.com/pablocorbalann/secgenda
"""
The config.py file contains all the configuration variables and statements
that are used in the application, if you are not sure about what do some of the 
sentences mean, better you don't touch anything :)
"""

# Enable the development enviroment of the flask server
DEBUG=True

# The configuration of the flask server
PORT=8080
HOSTNAME="127.0.0.1"

# Define the application directory using the OS library
import os
BASE_DIR = os.path.abspath(os.path.dirname(__name__))

# Application threads (don't touch it if you don't know what it is)
THREADS_PER_PAGE=2
