import pytest
from selenium import webdriver

browser = webdriver.Chrome()
#testing changes
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