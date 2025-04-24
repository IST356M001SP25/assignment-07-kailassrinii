import re
from playwright.sync_api import Playwright, sync_playwright
from menuitemextractor import extract_menu_item
from menuitem import MenuItem
import pandas as pd

def tullyscraper(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.tullysgoodtimes.com/menus/")

    # TODO Write code here
    all_menu_items = []
    
    title_selector = 'h3.heading' 
    titles = page.query_selector_all(title_selector)
    
    for title_element in titles:
        title = title_element.inner_text()
        menu_container = title_element.evaluate_handle('el => el.parentElement.nextElementSibling.nextElementSibling')
        items = menu_container.query_selector_all('.menu-item')
        
        for item in items:
            item_text = item.inner_text()
            menu_item = extract_menu_item(title, item_text)
            all_menu_items.append(menu_item.to_dict())
    

    df = pd.DataFrame(all_menu_items)## pandas 
    
    import os
    os.makedirs('cache', exist_ok=True)
    
    df.to_csv('../cache/tullys_menu.csv', index=False) ## csv
    print(f"Scraped {len(df)} menu items and saved to 'cache/tullys_menu.csv'")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    tullyscraper(playwright)
