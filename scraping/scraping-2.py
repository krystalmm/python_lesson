# 1,全カテゴリのURLと、カテゴリ名を取得する
# 2,カテゴリURLにアクセスする
# 3,カテゴリURLの記事のタイトルと、URLと、カテゴリ名を列に追加する
# 4,「次へ」があれば、次のページに遷移する
# 5,次のページがなくなるまで繰り返す
# 6,一つにカテゴリが終わったら、次のカテゴリへ移動する
# 7,全てのカテゴリが終わったら、終了する


import requests
import pandas as pd
from bs4 import BeautifulSoup

# print(requests.get("https://dividable.net/").text)

# カテゴリの中のURLと名前は(nav#category ul li a)の中に存在してるので、それらのaタグを取得！
category_li_path = "nav#category ul li a"
response = requests.get("https://dividable.net").text
soup = BeautifulSoup(response, 'html.parser')
soup.select(category_li_path)

# ループを回してそれぞれのカテゴリのページを取りに行くので、データを扱いやすいように辞書型のデータにURLとカテゴリを変換！
category_html_list = soup.select(category_li_path)
category_dict = {}
for category_html in category_html_list:
    category_dict[category_html.get("href")] = category_html.string
print(category_dict)

# カテゴリURLにアクセスする！（ここではPython学習のカテゴリページのみ！）
category_res = requests.get("https://dividable.net/category/python/").text
# print(category_res)

# カテゴリURLの記事のタイトルとURLとカテゴリ名を列に追加する！（後で実装！）

# 次へがあればクリックして次のページに飛ぶ！
# ※ちなみに、https://dividable.net/category/python/page/1 は存在しませんが、https://dividable.net/category/python/page/1にアクセスすると、https://dividable.net/category/python/ にリダイレクト（自動遷移）する！
# だから、次へが存在すればpage番号を+1してあげてデータを取得する！
# 次へのHTMLコード
# <div class="pagination">
#    <span class="page_num">Page 1 of 5</span>
#    <span class="current pager">1</span>
#    <a href="https://dividable.net/category/python/page/2/" class="pager">2</a>
#    <a href="https://dividable.net/category/python/page/3/" class="pager">3</a>
#    <a href="https://dividable.net/category/python/page/2/" class="next">次へ ›</a>
#    <a href="https://dividable.net/category/python/page/5/" class="last">最後へ »</a>
# </div>

# 次へボタンが存在するか確認！
soup = BeautifulSoup(category_res, 'html.parser')
a_next_tag = soup.find_all("a", {"class": "next"})
# print(a_next_tag)

# 次へが存在する場合は次のページへ、存在しない場合は処理を止める！
page_count = 1
category_res = ""
soup = ""
while True:
    category_res = requests.get("https://dividable.net/category/python/" + "page/" + str(page_count)).text
    soup = BeautifulSoup(category_res, 'html.parser')
    print("{} ページ目".format(page_count))
    post_tags = soup.select("div.post")
    for post_tag in post_tags:
        print(post_tag.select("h3")[0].text)
        print(post_tag.select("a")[0].get("href"))
        print("Python学習")
    a_next_tag = soup.find_all("a", {"class": "next"})
    if a_next_tag:
        page_count += 1
        continue
    break
print("完了")
