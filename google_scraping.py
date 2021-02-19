# スクレイピング

# urllibはURLを扱える組み込みモジュール！
import urllib.request

from bs4 import BeautifulSoup

class Scraper:
  # スクレイピング対象となるwebサイトのURLを受け取る（後からgoogleを引数に渡す！）
  def __init__(self, site):
    self.site = site

  # スクレイピングしたいタイミングで呼び出す！
  def scrape(self):
    r = urllib.request.urlopen(self.site)
    html = r.read()
    parser = "html.parser"
    sp = BeautifulSoup(html, parser)
    # aタグを集めるため引数に"a"としている！
    for tag in sp.find_all("a"):
      url = tag.get("href")
      if url is None:
        continue
      # htmlがurlに入っていたら表示する（例: index.html）
      if "html" in url:
        print("\n" + url)

news = "https://www.google.com/"
Scraper(news).scrape()
