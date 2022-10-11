
from bs4 import BeautifulSoup
import requests

date_requested = input("Which year do you want to travel ? Type the date in this format YYY-MM-DD:")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date_requested}/")
billboard_web_page = response.text

soup = BeautifulSoup(billboard_web_page, "html.parser")
song_titles = soup.find_all("h3", class_="a-no-trucate")
song_texts = [song.getText().strip() for song in song_titles]
for song in song_texts:
  print(song)
# with open('FilmsToWatch.txt', 'w', encoding="utf-8") as f:
#     for article in song_texts:
#         f.write(f"{article}\n")
