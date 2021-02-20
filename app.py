from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def set_chrome_options() -> None:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-setuid-sandbox")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument(r"user-data-dir=.\app")

    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options


if __name__ == "__main__":
    driver = webdriver.Chrome(options=set_chrome_options())
    # Do stuff with your driver
    print('start')
    driver.get("https://www.google.com")
    driver.save_screenshot("google.png")
    print('created screenshot')
    driver.quit()
    print('end')
