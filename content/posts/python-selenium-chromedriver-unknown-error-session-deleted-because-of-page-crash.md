Title: Python Selenium ChromeDriver unknown error: session deleted because of page crash
Slug: python-selenium-chromedriver-unknown-error-session-deleted-because-of-page-crash  
Date: 2020-09-11 21:01:03  
Authors: m157q  
Category: Note 
Tags: Python, Selenium, ChromeDriver, Heroku, error
Summary: Encountered this error while using Selenium with ChromeDriver on Heroku Free dyno.


# Error Message

```text
selenium.common.exceptions.WebDriverException: Message: unknown error: session deleted because of page crash
from unknown error: cannot determine loading status
from tab crashed
```

---

# TL;DR

Added these two arguments for Selenium ChromeOptions solved my problem.

```python
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
```

---

# Detail

- `--disable-dev-shm-usage`
    - > This will force Chrome to use the /tmp directory instead. This may slow down the execution though since disk will be used instead of memory.
- "from tab crashed"
    - > Relates to Linux attempting to always use /dev/shm for non-executable memory.

---

# References

- [python - unknown error: session deleted because of page crash from unknown error: cannot determine loading status from tab crashed with ChromeDriver Selenium - Stack Overflow](https://stackoverflow.com/questions/53902507/unknown-error-session-deleted-because-of-page-crash-from-unknown-error-cannot)
- [715363 - Chrome crashes/fails to load when /dev/shm is too small, and location can't be overridden](https://bugs.chromium.org/p/chromium/issues/detail?id=715363)
