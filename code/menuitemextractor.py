if __name__ == "__main__":
    import sys
    sys.path.append('code')
    from menuitem import MenuItem
else:
    from code.menuitem import MenuItem


def clean_price(price:str) -> float:
    price = price.replace('$', '')
    price = price.replace(',', '')
    return float(price)


def clean_scraped_text(scraped_text: str) -> list[str]:
    lines = scraped_text.split('\n')
    cleaned_lines = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line == "NEW!" or line == "NEW":
            continue
        if line in ["S", "V", "GS", "P"]:
            continue
        cleaned_lines.append(line)
    return cleaned_lines

def extract_menu_item(title:str, scraped_text: str) -> MenuItem:
    cleaned_text = clean_scraped_text(scraped_text)
    name = cleaned_text[0]
    price = clean_price(cleaned_text[1])

    if len(cleaned_text) > 2:
        description = cleaned_text[2]
    else:
        description = "No description available"
    
    return MenuItem(
        category=title,
        name=name,
        price=price,
        description=description
    )

if __name__=='__main__':
    pass
