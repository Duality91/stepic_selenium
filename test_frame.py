from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

browser = webdriver.Chrome()
browser.implicitly_wait(5)


def test_reg1():
    url = "http://suninjuly.github.io/registration1.html"
    browser.get(url)
    browser.fullscreen_window()

    fi_nam = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'first')]")
    fi_nam.send_keys("Ivan")
    la_nam = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'last')]")
    la_nam.send_keys("Petrow")
    email = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'email')]")
    email.send_keys("test@test.ru")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text, "User can`t log in"

def test_reg2():
    url = "http://suninjuly.github.io/registration2.html"
    browser.get(url)
    browser.fullscreen_window()

    fi_nam = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'first')]")
    fi_nam.send_keys("Ivan")
    la_nam = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'last')]")
    la_nam.send_keys("Petrow")
    email = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'email')]")
    email.send_keys("test@test.ru")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
   button.click()

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text, "User can`t log in"
    browser.quit()


if __name__ == "__main__":
    pytest.main()
