# Py-Easy-Scrape

## Description

__A useful package for web scraping with Selenium.__

This package provides useful wrapping of some of the more cumbersome aspects of using Selenium directly, such as initializing the WebDriver, scrolling, and handling elements.

Also, it simplifies some common tasks in web scraper bots, such as  asking the user to manually input some data when necessary and checking if some file exists in the user's computer.

Moreover, it kind of does the same with Logging: Py Easy Scrape comes with built-in logging, which can be a significant advantage for quickly deploying, debugging, and monitoring your web scraping project!

## Installation

```bash
pip install py-easy-scrape
```

## Requirements

- Python 3.7 or higher
- Selenium, along with __GeckoDriver__ (Firefox)

## Usage

Py-Easy-Scrape has a built-in logging system that, so far, needs a directory for all the logs that are going to be generated. Hence, in your project directory, create a new directory called 'logs':
```bash
mkdir logs
```

Then, import the package:
```python
import pyeasyscrape as pes
```

### Get WebDriver

```python
driver = pes.get_webdriver(headless=True)
```
This will return a headless instance of webdriver.Firefox (GeckoDriver).

### Get Element

```python
element = pes.get_element(driver, value="element_xpath")
```

This will return the web element found using the specified driver and value. By default, this function uses 'XPATH' as the method of searching. However, you can change this by providing 'ID' or 'LINK_TEXT' as the 'by' argument.

Please be aware that the method of searching ('XPATH', 'ID', or 'LINK_TEXT') highly depends on the webpage structure. Therefore, it is essential to inspect the webpage beforehand.

Also, please remember to replace `"element_xpath"` with the actual Xpath, ID, or link text of the element you want to find.

### Check Element

```python
is_clickable = check_element(driver, xpath="element_xpath")
```

This will return `True` if the web element specified by the XPath is found, displayed, and clickable using the provided driver. If not, it will return `False`. 

Alternatively, you can directly pass a web element object:

```python
is_clickable = check_element(driver, web_element=element)
```

Please replace `"element_xpath"` with the actual XPath of the element you want to check. This method ensures the element is both present and interactive before performing further actions.


### Scroll to Element

```python
pes.scroll_to(driver, element)
```

This will use JavaScript to scroll the view of the given webdriver to the specified web element.

### Ask for Data

```python
required_data = ("username", "password")
file_name_no_extension = "user_credentials"
pes.ask_for_data(required_data, file_name_no_extension)
```

This will return a dictionary containing the collected data and will create a JSON configuration (.conf) file.

### Check File

```python
pes.check_file("path_to_file")
```

This will return either True or False based on file existence

Please note that the above code snippets are basic examples of how to use those functions. Depending on the exact specifications of your use case, additional setup may be necessary (e.g. logging into a website before trying to scroll to an element).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT

