# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Test():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_(self):
    self.driver.get("https://qa.neapro.site/cabinet/documents")
    self.driver.find_element(By.CSS_SELECTOR, ".form:nth-child(3) .document-tile:nth-child(1) > .document-status").click()
    time.sleep(NaN)
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)").click()
    self.vars["win7743"] = self.wait_for_window(2000)
    self.vars["root"] = self.driver.current_window_handle
    self.driver.switch_to.window(self.vars["win7743"])
    self.driver.close()
    self.driver.switch_to.window(self.vars["root"])
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "input").send_keys("C:\\Users\\Сергей\\Desktop\\contract.pdf")
    self.driver.find_element(By.CSS_SELECTOR, ".fill").click()
  
