from scrapper import fetch_content
from aiwriter import rewrite_text
from aireviewer import aitext_reviewer

URL = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
text, image = fetch_content(URL)
print(text[:1000])

print("sending the chapter for rewriting to genini")
aiwritten_text = rewrite_text(text)

with open("data/chapter_spun.txt", "w", encoding="utf-8") as f:
    f.write(aiwritten_text)

review = aitext_reviewer(aiwritten_text)

# Save review
with open("data/chapter_review.txt", "w", encoding="utf-8") as f:
    f.write(review)