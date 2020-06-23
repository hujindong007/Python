from selenium import webdriver
import time

username = "12344"
password = "12344"

driver = webdriver.Chrome()
driver.get('https://www.douban.com/')
iframe = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(iframe)
# driver.find_element_by_css_selector('li.account-tab-account').click()  # 点击密码登录的标签
# driver.find_element_by_class_name('account-tab-account').click()
# driver.find_element_by_id('username').send_keys(username)
# driver.find_element_by_id('password').send_keys(password)
# driver.find_element_by_class_name('btn-account').click()

driver.find_element_by_class_name("account-tab-phone").click()
# phoneName = driver.find_elements_by_class_name("account-form-input")[0]
# print(phoneName.send_keys(username))
# driver.find_element 默认取第一个
driver.find_element_by_class_name("account-form-input").send_keys(username)

driver.find_element_by_id("code").send_keys(password)


# 获取cookies,字典推导式
cookies = {i['name']: i['value'] for i in driver.get_cookies()}
print(cookies)
time.sleep(5)
driver.quit()