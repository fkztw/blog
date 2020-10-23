Title: Bypass Cloudflare detection while using Selenium with ChromeDriver  
Slug: bypass-cloudflare-detection-while-using-selenium-with-chromedriver  
Date: 2020-09-11 21:25:46  
Authors: m157q  
Category: Note  
Tags: Selenium, Python, ChromeDriver, Cloudflare  
Summary: I was blocked by Cloudflare while scraping some websites and this saved me. So, I am gonna write it down.  
Modified: 2020-10-24 00:34:46  


# TL;DR

```python
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
```

---

# Complete Code Example

```python
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)
driver.get(URL)
```

---

# Detail

- `options.add_experimental_option("excludeSwitches", ["enable-automation"])`
    - > Exclude the collection of enable-automation switches
- `options.add_experimental_option('useAutomationExtension', False)`
    - > Turn-off useAutomationExtension
- `options.add_argument("--disable-blink-features=AutomationControlled")`
    - > Make `navigator.webdriver=undefined` in webdriver console

---

# References

- [java - Selenium webdriver: Modifying navigator.webdriver flag to prevent selenium detection - Stack Overflow](https://stackoverflow.com/questions/53039551/selenium-webdriver-modifying-navigator-webdriver-flag-to-prevent-selenium-detec/53040904#53040904)
- - [java - Selenium webdriver: Modifying navigator.webdriver flag to prevent selenium detection - Stack Overflow](https://stackoverflow.com/questions/53039551/selenium-webdriver-modifying-navigator-webdriver-flag-to-prevent-selenium-detec/60403652#60403652)
