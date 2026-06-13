from playwright.sync_api import expect, sync_playwright
import re

browser_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def getPrice(page, product_name):
    page.goto("https://www.demoblaze.com/")
    page.locator("list-group-item").click()
    product_card_class = "card h-100"
    product = page.locator(product_card_class, has_text=product_name).first
    expect(product).to_be_visible(timeout=10000)  # Wait until the product card is visible

    product_text = product.inner_text()
    match = re.search(r"$s*[\d,]+", product_text)

    if match:
        price_text = match.group()
        price_number = re.sub(r"[^\d]", "", price_text)
        return float(price_number)

def checkPrice(page,product_name):
    gotPrice=getPrice(page,product_name)

    if gotPrice==700:
        print("Success")
    else:
        print("Failed")


if __name__ == "__main__":
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(
            headless=False, 
            slow_mo=500
        )
        main_page = browser.new_page()

        




        main_page.wait_for_timeout(5000)
