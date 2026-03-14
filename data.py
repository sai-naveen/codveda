import requests
from bs4 import BeautifulSoup
import csv

url = "https://news.ycombinator.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("span", class_="titleline")

with open("news_headlines.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["News Headlines"])

    for title in titles:
        writer.writerow([title.text])

print("Scraping completed. Data saved in news_headlines.csv")