from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


uploader = '美食作家王刚R'
lst = []

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)

    driver.get('https://search.bilibili.com/')

    driver.find_element_by_id('search-keyword').send_keys(uploader)
    driver.find_element_by_xpath('//*[@id="server-search-app"]/div[2]/div/div[2]/a').click()
    driver.find_element_by_xpath('//*[@id="server-search-app"]/div[2]/div[2]/div/div[2]/ul[4]/li/div[2]/div[1]/a[1]').click()

    #获取当前页面句柄
    window_1 = driver.current_window_handle
    #获取所有页面句柄
    windows = driver.window_handles
    for current_window in windows:
        if current_window != window_1:
            driver.switch_to.window(current_window)

    more_button = WebDriverWait(driver, 10)\
        .until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="page-index"]/div[1]/div[1]/h3/a[2]')))
    more_button.click()

    elements = driver.find_elements_by_xpath('//*[@id="submit-video-list"]/ul[2]')
    for element in elements:
        # av_id = element.get_attribute('data-aid')
        # av_title = element.get_attribute('title')
        className = element.get_attribute('src')
        print(element.text)



