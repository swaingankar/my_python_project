import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.headless = True

browser = webdriver.Chrome(options=chrome_options)
# browser = webdriver.Chrome()

def test_open_url():
	url = "http://blazedemo.com/"
	browser.get(url)

	assert browser.current_url == url

def test_open_url_fail():
	url = "http://blazedemo.com/"
	browser.get(url)

	assert browser.current_url != url

def test_close_browser():
	browser.close()
	browser.quit()
