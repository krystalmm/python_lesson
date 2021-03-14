from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
# BeautifulSoupの初期化
soup = BeautifulSoup(html_doc, 'html.parser')

# HTMLをきれいにインデントする！
print(soup.prettify())

# <title>The Dormouse’s story</title>を取得してprintする
print(soup.title)

#  The Dormouse’s story を取得してprintする
print(soup.title.string)

# すべてのaタグを取得（リスト形式でかえってくる！）
print(soup.find_all("a"))

# aタグを一つ一つ取得する
a_list = soup.find_all("a")
# HTMLを含む
print("1,")
for a in a_list:
    print(a)

# HTMLを含まない
print("2,")
for a in a_list:
    print(a.string)

# aタグのhrefのURLだけ取得する
print(soup.a.get("href"))

# すべてのURLをprintする
print("3,")
for a in a_list:
    print(a.get("href"))



