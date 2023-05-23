import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    request.instance.driver = driver
    yield driver
    driver.close()

@pytest.mark.usefixtures("setup")
class Test:
    def test_example(self):
        self.driver.get('https://bstackdemo.com/')
        productText = self.driver.find_element(By.XPATH, '//*[@id="1"]/p').text
        self.driver.find_element(By.XPATH, '//*[@id="1"]/div[4]').click()
        self.driver.find_element(By.CLASS_NAME, 'float-cart__content')
        productCartText = self.driver.find_element(By.XPATH,
                                              '//*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/div[3]/p[1]').text

        assert productCartText == productText

