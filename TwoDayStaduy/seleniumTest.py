from selenium import webdriver
# import time
# from selenium.webdriver import Firefox
#from selenium.webdriver import Chrome

# browser = webdriver.Firefox(executable_path='/usr/local/Cellar/geckodriver/0.26.0/bin/geckodriver')
#
# browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
# browser = webdriver.Firefox()
#browser = Chrome(executable_path='/usr/local/bin/chromedriver')
browser = webdriver.Chrome()
browser.get("https://www.baidu.com")
browser.find_element_by_id("kw").send_keys("python")
browser.find_element_by_id("su").click()


# time.sleep(3)
# browser.quit()
