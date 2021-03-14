# requestsはwebページからデータを取得する！
# Beautifulsoupは取得したHTMLのデータの中からタグを読み取り、操作することができる!


import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

# response = requests.get("https://review-of-my-life.blogspot.com/")
# requestsで取得したデータをprint
# print(response.text)

# 上のHTMLをきれいにする
# 読み込む際には.textが必要！！！
html_doc = requests.get("https://review-of-my-life.blogspot.com/").text
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())

# aタグを抜き出す
tags = soup.find_all("a")

for tag in tags:
    print("1,")
    print(tag)
    print("2,")
    print(tag.string)
    print("3,")
    print(tag.get("href"))


# 記事のタイトルのみを取得する（h3タグのclass=post-title）
print(soup.find_all("h3", {"class": "post-title"}))

# 記事を一つずつ抜き出す（記事名とURLの取得！）
heads = soup.find_all("h3", {"class": "post-title"})

for head in heads:
    print("1,")
    print(head.a.string)
    print("2,")
    print(head.a.get("href"))


# pandasを使ってcsvにデータを保存する
# まずは列名を作成！
columns = ["Name", "Url"]
df = pd.DataFrame(columns=columns)
# print(df)

# 次に行を追加
# se = pd.Series(['記事のタイトル', 'http://URL'], columns)
# df = df.append(se, columns)
# print(df)

# 上の記事のタイトルとURLを使ってデータフレームを作成する！
for head in heads:
    se = pd.Series([head.a.string, head.a.get("href")], columns)
    df = df.append(se, columns)
    # print(df)

# 作成したデータフレームをcsvに変換！
filename = "scraping-1-exercise.csv"
df.to_csv(filename, encoding = 'utf-8-sig')
# ファイルをダウンロードする
