# 全カテゴリからデータを収集する！

import requests
import pandas as pd
from bs4 import BeautifulSoup

# url, title, categoryを列に持ったDataFrameを作成！
columns = ["Url", "Title", "Category"]
df = pd.DataFrame(columns=columns)

# カテゴリURLとカテゴリ名を持った辞書型オブジェクトを作成！
category_li_path = "nav#category ul li a"
res = requests.get("https://dividable.net").text
soup = BeautifulSoup(res, 'html.parser')
category_html_list = soup.select(category_li_path)
category_dict = {}
for category_html in category_html_list:
    category_dict[category_html.get("href")] = category_html.string

# カテゴリを一つ一つ取り出して、ページャーの最後まで記事を取得する！
for key, value in category_dict.items():
    print("-----カテゴリ: {} -------".format(value))
    page_count = 1
    category_res = ""
    soup = ""
    while True:
        print("------{} ページ目 -------".format(page_count))
        category_res = requests.get(key + "/page/" + str(page_count)).text
        soup = BeautifulSoup(category_res, 'html.parser')
        post_tags = soup.select("div.post")
        for post_tag in post_tags:
            title = post_tag.select("h3")[0].text
            url = post_tag.select("a")[0].get("href")
            se = pd.Series([title, url, value], columns)
            df = df.append(se, ignore_index=True)
        a_next_tag = soup.find_all("a", {"class": "next"})
        if a_next_tag:
            page_count += 1
            continue
        break
print("完了")

# result.csvというファイル名でcsvに記事を保存する！
df.to_csv("result.csv", encoding = 'utf-8-sig')