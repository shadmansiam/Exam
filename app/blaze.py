from playwright.sync_api import expect
import re

class Blaze:
    def __init__(self):
        self.url = "https://www.demoblaze.com"
        self.search_placeholder = ""
        self.product_card_class = "card h-100"

    def open_site(self, page):
        page.goto(self.url, wait_until="domcontentloaded")   

    def get_product_card(self, page, product_name):
        product = page.locator(self.product_card_class, has_text=product_name).first
        expect(product).to_be_visible(timeout=10000)  # ei line ki kore?
        return product
    
    def get_product_price_text(self, page, product_name):
        product = self.get_product_card(page, product_name)
        product_text = product.inner_text()

        match = re.search(r"৳\s*[\d,]+", product_text)

        if match:
            return match.group()

        raise AssertionError(f"Price not found for product: {product_name}")  # ki kore?
    
    def get_product_price(self, page, product_name):
        price_text = self.get_product_price_text(page, product_name)
        price_number = re.sub(r"[^\d]", "", price_text)
        return int(price_number)