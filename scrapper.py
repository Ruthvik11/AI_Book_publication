from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import os


def fetch_content(url, save_dir="data"):
    os.makedirs(save_dir,exist_ok=True)
   
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = True)
        page = browser.new_page()
        page.goto(url)

        screenshot_path = os.path.join(save_dir, "chapter.png")
        page.screenshot(path=screenshot_path, full_page = True)


        html = page.content()
        browser.close()
    soup = BeautifulSoup(html, "html.parser")
    content_div = soup.find("div", class_="mw-parser-output")

    if not content_div:
        print("Could not find main content area.")
        return None, None

    paragraphs = content_div.find_all("p")
    chapter_text = "\n\n".join([p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)])


    text_path = os.path.join(save_dir,"chapter1.txt")
    with open(text_path,"w",encoding="utf-8") as f:
        f.write(chapter_text)
    
    return chapter_text, screenshot_path