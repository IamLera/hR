from selenium.webdriver.common.by import By


class LoginPageLocators():
    emailField = (By.CSS_SELECTOR, ".mantine-TextInput-root input")
    passwordField = (By.CSS_SELECTOR, ".mantine-PasswordInput-input input")
    loginBtn = (By.CSS_SELECTOR, "button[aria-label='log in']")
    errorMsg = (By.CSS_SELECTOR, ".mantine-Alert-message")