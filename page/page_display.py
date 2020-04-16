
class Page_display:

    def __init__(self, driver):
        self.driver = driver

    def click_display(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()

    def click_search(self):
        self.driver.find_element_by_id("com.android.settings:id/search").click()

    def click_explore(self,text):
        self.driver.find_element_by_xpath("//*[contains(@text,'搜索')]").send_keys(text)

    def click_back(self):
        self.driver.find_element_by_class_name("android.widget.ImageButton").click()