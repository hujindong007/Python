from selenium import webdriver
import time


# browser = webdriver.Firefox(executable_path='/Users/fangsu/Desktop/TestSelenium/spider/geckodriver')
#
# browser = webdriver.Chrome(executable_path='/Users/fangsu/Desktop/TestSelenium/spider/chromedriver')



# browser_path = "/usr/local/bin/chromedriver"
# browser = webdriver.Chrome(browser_path)
browser = webdriver.Chrome()
# browser.get_window_size(1920,1080)#设置屏幕宽高
# browser.maximize_window()#设置最大
# browser.save_screenshot("./baidu.png")#截屏
# browser.get("https://www.baidu.com")
#
# browser.find_element_by_id("kw").send_keys("python")
# browser.find_element_by_id("su").click()
# print("当前网址",browser.current_url)
# print("下一页网址：",browser.find_element_by_link_text("下一页>").get_attribute("href"))


browser.get("https://www.douban.com/")
browser.find_element_by_xpath("//*[@id=\"anony-nav\"]/div[2]/form/span[1]/input").send_keys("1234")
browser.find_element_by_xpath("//*[@id=\"anony-nav\"]/div[2]/form/span[2]/input").click()







time.sleep(3)
# print("下一页网址：",browser.find_element_by_link_text("下一页>").get_attribute("href"))
# browser.close()#退出当前页
browser.quit()#退出浏览器