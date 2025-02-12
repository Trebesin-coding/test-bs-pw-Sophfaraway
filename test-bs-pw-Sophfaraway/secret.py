from playwright.sync_api import sync_playwright
import os




def main():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://js-trebesin.github.io/playwright-exam/")

        password = "Admin123"
        username = "Jarmil"

        page.fill("input[id='login']", username)
        page.fill("input[id='pass']", password)

        page.click("button[class='login-btn']")
        
        secret = page.locator("body > div > div > p").text_content()
        print(secret)


        # !!!
        # na page.locator(selector) se dá použít funkce .text_content(), která vypíše text daného prvku
        # !!!

        input("dont close right away")
        browser.close()
    

if __name__ == "__main__":
    main()
