from app.blaze import Blaze

def test_blaze_product_price(page):
    blaze_page=Blaze()

    product_name = "HTC One M9"
    expected_price = 700

    blaze_page.open_site(page)
    actual_price=blaze_page.get_product_price(page,product_name)

    assert actual_price == expected_price

def test_blaze_product_price_failure(page):
    blaze_page=Blaze()

    product_name = "HTC One M9"
    expected_price = 800

    blaze_page.open_site(page)
    actual_price=blaze_page.get_product_price(page,product_name)

    assert actual_price == expected_price