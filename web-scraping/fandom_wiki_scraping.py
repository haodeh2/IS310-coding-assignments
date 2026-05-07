from bs4 import BeautifulSoup
import cloudscraper
import csv

scraper = cloudscraper.create_scraper()

url = "https://fruitsbasket.fandom.com/wiki/Category:Fruits_Basket_Characters"

response = scraper.get(url, timeout=10)

print(response.status_code)
print(response.url)
soup = BeautifulSoup(response.text, "html.parser")

characters = soup.find_all("a", class_="category-page__member-link")

character_data = []

for character in characters:
    name = character.get_text()
    link = character.get("href")

    character_data.append({
        "name": name,
        "link": "https://fruitsbasket.fandom.com" + link
    })

# print(character_data)

with open("web-scraping/fruits_basket_characters.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "link"])

    for character in character_data:
        writer.writerow([character["name"], character["link"]])

print("CSV file created successfully!")