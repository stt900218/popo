import pytest
import os, sys
sys.path.append(os.getcwd())
from base.base_driver import init_driver
from appium import webdriver
from page.page_network import PageNetwork


class TestNetwork:
    def setup(self):
        self.driver = init_driver()
        self.myPageNetwork = PageNetwork(self.driver)

    def test_mobile_network_2g(self):

        self.myPageNetwork.click_more()
        self.myPageNetwork.click_mobile_network()
        self.myPageNetwork.click_first()
        self.myPageNetwork.click_2G()

    def test_mobile_network_3g(self):

        self.myPageNetwork.click_more()
        self.myPageNetwork.click_mobile_network()
        self.myPageNetwork.click_first()
        self.myPageNetwork.click_3G()


