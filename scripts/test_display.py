import pytest
import os, sys
sys.path.append(os.getcwd())

from appium import webdriver
from base.base_driver import init_driver
from page.page_display import Page_display


class TestDisplay:
    def setup(self):
        self.driver = init_driver()
        self.myPage = Page_display(self.driver)

    def test_mobile_display_input(self):
        self.myPage.click_display()
        self.myPage.click_search()
        self.myPage.click_explore("hello")
        self.myPage.click_back()




