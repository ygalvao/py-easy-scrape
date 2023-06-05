#!/usr/bin/env python3

#************************************************************#
#                                                            #
# Written by Yuri H. Galvao <yuri@galvao.ca>, March 2023     #
#                                                            #
#************************************************************#

import os, json, sys, time, logging, traceback
from datetime import datetime
from contextlib import contextmanager

args = sys.argv[1:] # List of arguments that were passed

yes_for_all = True if '--yes-for-all' in args else False
log_dir = args[args.index('--log-dir')+1] if '--log-dir' in args else 'logs' # The directory where the log files will be saved

# Declaring and configuring the logger
class FileHandlerNotEmpty(logging.FileHandler):
    def __init__(self, filename, mode='a', encoding=None, delay=False):
        self.fname = filename
        self.has_error = False
        super().__init__(filename, mode, encoding, delay)

    def emit(self, record):
        if record.levelno >= logging.ERROR:
            self.has_error = True
        super().emit(record)

    def close(self):
        super().close()
        if not self.has_error:
            os.remove(self.fname)

now = datetime.now().strftime("%Y-%m-%d_-_%H_%M")
log_file_name = f'{now}.log'
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
file_handler = FileHandlerNotEmpty(f'{log_dir}/{log_file_name}')
console_handler = logging.StreamHandler(sys.stdout)
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

debug = lambda msg: logger.debug(msg)
info = lambda msg: logger.info(msg)
warning = lambda msg: logger.warning(msg)
error = lambda msg: logger.error(msg)
critical_error = lambda msg: logger.critical(msg)

def confirm(text:str)->bool:
    """
    Checks if a file exists in the current directory.

    Arguments:
        file (str): The name of the file to check.

    Returns:
        bool: True if the file exists, False otherwise.
    """

    confirm = 'y' if yes_for_all else input(text)
    
    if confirm.lower() not in ('n', 'no'):
        return True
    else:
        return False

def check_file(path_to_file:str)->bool:
    """
    Checks if a file exists in the current directory.

    Arguments:
        file (str): The name of the file to check.

    Returns:
        bool: True if the file exists, False otherwise.
    """

    if os.path.isfile('./' + path_to_file):
        return True
    else:
        return False

def ask_for_data(required_data:tuple, file_name_no_extension:str, ask:bool=True)->dict:
    """
    Asks the user for input, creates a JSON configuration file, and returns the input as a dictionary.

    Args:
        required_data (tuple): The data to be collected from the user.
        file_name_no_extension (str): The name of the configuration file without the extension.
        ask (bool, optional): Whether to ask for user input or use default values. Defaults to True.

    Returns:
        dict: A dictionary containing the collected data.
    """

    data_dict = {}
    if ask:
        for data in required_data:
            data_dict[data] = input(f'Enter the {data}: ')

        json.dump(data_dict, open(f'config/{file_name_no_extension}.conf', 'w'))
    else:
        for data in required_data:
            data_dict[data[0]] = data[1]

        json.dump(data_dict, open(f'config/{file_name_no_extension}.conf', 'w'))
    
    print()

    return data_dict

def list_from_input(text:str)->list:
    """
    Converts a comma-separated user input string into a list.

    Arguments:
        text (str): The text to be displayed as a prompt for user input.

    Returns:
        list: A list containing the user input as integers or strings.
    """

    raw_list = input(text)

    try:
        final_list = [int(n) for n in raw_list.replace(' ', '').split(',')]
    except:
        final_list = [str(s) for s in raw_list.replace(' ', '').split(',')]

    return final_list

@contextmanager # A function that creates generators (and use them to iterate instead of lists of web elements) was one of the ways that I found to prevent memory leak when unsing Selenium
def generator(list_:list):
    """Creates a generator from a list"""
   
    yield list_
