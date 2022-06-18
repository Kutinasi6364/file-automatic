import requests 
import time
from bs4 import BeautifulSoup 

# 画像を保存するフォルダ作成用
from pathlib import Path 

# スクレイピングを行うURL
base_url = "https://kutinasi-hobbyjoy.com/"

# フォルダ名を指定
folder = Path("blog_image")

#フォルダが存在しない場合作成
folder.mkdir(exist_ok = True)

response = requests.get(base_url)
soup = BeautifulSoup(response.content, "html.parser")

image_sorce = soup.find_all(class_="entry-card-thumb-image")

for images in image_sorce:
  image_url = images.get("data-src")
  if image_url is None:
    continue
  
  image = requests.get(image_url)
  
  with open(str("./blog_image/") + str(time.time())[-6:] + str(".jpeg"),"wb") as file: 
    file.write(image.content)

    
 
