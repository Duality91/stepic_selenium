# import math
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import os
# from selenium.webdriver.support.ui import Select
#
# try:
#     browser = webdriver.Chrome()
#     link = "http://suninjuly.github.io/file_input.html"
#     browser.get(link)
#     browser.execute_script("window.scrollBy(0, 150);")
#     browser.fullscreen_window()
#     # x = browser.find_element(By.CSS_SELECTOR, "span#input_value").text
#     input_fnm = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']").send_keys("Rita")
#     input_snm = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']").send_keys("Test")
#     input_mail = browser.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("test@test.ru")
#     button_add_file = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
#
#     current_dir = os.path.abspath(os.path.dirname(__file__))
#     file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
#     button_add_file.send_keys(file_path)
#
#     submit_but = browser.find_element(By.TAG_NAME, "button")
#     submit_but.click()
#
# finally:
# # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(6)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#     print()

# import math
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import os
# from selenium.webdriver.support.ui import Select
#
# try:
#     browser = webdriver.Chrome()
#     link = "http://suninjuly.github.io/alert_accept.html"
#     browser.get(link)
#     browser.execute_script("window.scrollBy(0, 150);")
#     browser.fullscreen_window()
#
#     button_click = browser.find_element(By.TAG_NAME, "button").click()
#     confirm = browser.switch_to.alert
#     confirm.accept()
#     browser.fullscreen_window()
#
#     def calc(x):
#         return str(math.log(abs(12 * math.sin(int(x)))))
#
#
#     x = browser.find_element(By.CSS_SELECTOR, 'span#input_value').text
#     y = calc(int(x))
#     fill_form = browser.find_element(By.CSS_SELECTOR,'input.form-control').send_keys(y)
#     button_submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
#
#
# finally:
# # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(6)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#     print()
#
# import math
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import os
# from selenium.webdriver.support.ui import Select
#
# try:
#     browser = webdriver.Chrome()
#     link = "http://suninjuly.github.io/redirect_accept.html"
#     browser.get(link)
#     browser.execute_script("window.scrollBy(0, 150);")
#     browser.fullscreen_window()
#
#     button_click = browser.find_element(By.TAG_NAME, "button").click()
#     # confirm = browser.switch_to.alert
#     # confirm.accept()
#     # browser.fullscreen_window()
#     new_window = browser.window_handles[1]
#     browser.switch_to.window(new_window)
#     def calc(x):
#         return str(math.log(abs(12 * math.sin(int(x)))))
#
#
#     x = browser.find_element(By.CSS_SELECTOR, 'span#input_value').text
#     y = calc(int(x))
#     fill_form = browser.find_element(By.CSS_SELECTOR,'input.form-control').send_keys(y)
#     button_submit = browser.find_element(By.TAG_NAME, "button").click()
#
#
# finally:
# # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(6)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#     print()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# browser.implicitly_wait(5)
# browser.get("http://suninjuly.github.io/cats.html")
#
# browser.find_element(By.ID, "button")
#
# browser.quit()
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
browser.fullscreen_window()
browser.execute_script("window.scrollBy(0, 150);")

try:
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button = browser.find_element(By.ID, "book")
    button.click()
    browser.save_screenshot("booking.png")

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = browser.find_element(By.CSS_SELECTOR, 'span#input_value').text
    y = calc(int(x))
    fill_form = browser.find_element(By.CSS_SELECTOR,'input.form-control').send_keys(y)
    button_submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()


finally:
    time.sleep(3)
    # browser.quit()