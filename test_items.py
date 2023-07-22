from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_browser_title(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    button_cart = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")

    assert button_cart.is_displayed(), "Кнопка добавления в корзину не найдена на странице"

