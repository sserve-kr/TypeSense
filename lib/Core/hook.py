from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome('assets\\driver.exe')
driver.get("http://s0urce.io")

window_xpath = '//*[@id="window-tool"]'
input_xpath = '//*[@id="tool-type-word"]'
word_xpath = '//*[@id="tool-type"]/img'
target_window_xpath = '//*[@id="window-list"]'
target_window_close_xpath = '//*[@id="topwindow-success"]/div/div[1]/span'

login_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'login-play')))
while login_button.is_displayed():
    sleep(3)
    print('Waiting for log-in...')
console = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, window_xpath)))
input_box = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, input_xpath)))
word_img = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, word_xpath)))
target_msg = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'targetmessage-input')))
target_msg_btn = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'targetmessage-button-send')))
target_msg_window_close = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,
                                                                                          target_window_close_xpath)))
target_list = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CLASS_NAME,
                                                                                   'window-list-table-select')))
target_list_window = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, target_window_xpath)))
portA = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="window-other-port1"]')))
portB = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="window-other-port2"]')))
portC = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="window-other-port3"]')))


def get_image_url():
    return word_img.get_attribute('src')


def hack_available():
    if 'template.png' in get_image_url():
        return False
    elif not console.is_displayed():
        return False
    elif not input_box.is_enabled():
        return False
    else:
        return True
