#!/usr/bin/env python3

#************************************************************#
#                                                            #
# Written by Yuri H. Galvao <yuri@galvao.ca>, May 2023       #
#                                                            #
#************************************************************#

# Importing from modules / packages
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from basic_functions import *

def get_webdriver(headless:bool)->object:
    """
    Sets up and returns a selenium webdriver object with desired configurations. Uses GeckoDriver (Firefox).

    Arguments:
        headless (bool): Whether to run the webdriver in headless mode.

    Returns:
        object: An instance of webdriver.Firefox with specified options.
    """

    # Declaring some important variables for the Gecko Webdriver (Firefox)
    options = Options()
    #linux_useragent = "Mozilla/5.0  (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.download.dir", DOWNLOAD_DIRECTORY+'/raw')
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")
    options.add_argument('disable-infobars')
    options.add_argument('--disable-extensions')
    #options.add_argument(f'user-agent={linux_useragent}')
    options.add_argument('--no-sandbox')

    if headless is True:
        options.add_argument('--headless')

    driver = webdriver.Firefox(options = options)
    driver.set_window_size(1920,1040)

    return driver

def scroll_to(driver:object, element:object)->None:
    """
    Scrolls the view of a given webdriver to a specific web element.

    Arguments:
        driver (object): The webdriver instance to scroll.
        element (object): The web element to scroll to.
        
    Returns:
        None
    """

    time.sleep(.05)
    x = element.location['x']
    y = element.location['y']
    scroll_by_coord = 'window.scrollTo(%s,%s);' % (x,y)
    scroll_nav_out_of_way = 'window.scrollBy(0, -120);'
    try:
        driver.execute_script(scroll_by_coord)
        driver.execute_script(scroll_nav_out_of_way)
    except:
        error('Error when scrolling to element!')

    time.sleep(.15)

def get_element(driver:object, value:str, by:str='XPATH')->object:
    """
    Returns a specific web element from a given webdriver by its value and method of searching.

    Arguments:
        driver (object): The webdriver instance to search in.
        value (str): The value to search for.
        by (str, optional): The method of searching. Can be 'XPATH', 'ID', or 'LINK_TEXT'. Defaults to 'XPATH'.

    Returns:
        object: The web element found.
    """

    i = 0
    element = None
    while not element:
        try:
            time.sleep(.5)
            if by == 'XPATH':
                element = driver.find_element(by=By.XPATH, value=value)
            if by == 'ID':
                element = driver.find_element(by=By.ID, value=value)
            if by == 'LINK_TEXT':
                element = driver.find_element(by=By.LINK_TEXT, value=value)

            i += 1
        except:
            i += 1
            continue
        finally:
            if i > 14:
                raise TimeoutError
    
    return element

def check_element(driver:object, xpath:str='', web_element:object=None)->bool:
    """
    Checks the existence and clickability of a specific web element in a given webdriver.

    Arguments:
        driver (object): The webdriver instance to check in.
        xpath (str, optional): The xpath of the element to check. Defaults to ''.
        web_element (object, optional): The web element to check. If not provided, will search for the element using xpath. 

    Returns:
        bool: True if the element exists and is clickable, False otherwise.
    """

    try:
        if xpath != '':
            element = WebDriverWait(driver, timeout=1).until(lambda x: x.find_element(by=By.XPATH, value=xpath))
        else:
            element = web_element

        scroll_to(driver, element)
        if not element.is_displayed():
            raise Exception

        if not element.is_enabled():
            raise Exception

        if xpath != '':
            WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, xpath)))

    except:
        return False
    else:
        return element