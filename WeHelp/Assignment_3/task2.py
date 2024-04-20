import urllib.request as req
import bs4
import csv

URL = f"https://www.ptt.cc/bbs/Lottery/index.html"

with open('article.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)

    num_pages_to_crawl = 3  # 設定要爬取的頁數

    for _ in range(num_pages_to_crawl):
        headers = {
            "cookie": "over18=1;",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
        }
        request = req.Request(URL, headers=headers)
        with req.urlopen(request) as response:
            data = response.read().decode("utf-8")

        soup = bs4.BeautifulSoup(data, "html.parser")
        articles = soup.find_all("div", class_="r-ent")

        for article in articles:
            try:
                '''<div class="title">
                                 <a href="/bbs/Lottery/M.1712222673.A.1C1.html">[報牌] 享受輸的感覺539</a>
                                </div>
                '''
                title_element = article.find("div", class_="title").a
                if title_element:
                    title = title_element.text.strip()
                    if "(本文已被刪除)" in title:
                        print(f"跳過已刪除文章: {title}")
                        continue

                    # 抓推文數
                    like_and_dislike = article.find(
                        "div", class_="nrec").text.strip()

                    link = title_element["href"]  # 抓取標題的連結
                    article_url = "https://www.ptt.cc" + link  # 將相對URL轉換成完整URL

                    article_request = req.Request(article_url, headers=headers)
                    with req.urlopen(article_request) as article_response:
                        article_data = article_response.read().decode("utf-8")

                    article_soup = bs4.BeautifulSoup(
                        article_data, "html.parser")

                    # 接下來要進去內文後，抓取標題、時間
                    meta_elements = article_soup.find_all(
                        "span", class_="article-meta-value")  # article-meta-value: 作者、看板、標題、時間

                    if meta_elements and len(meta_elements) >= 4:
                        date = meta_elements[3].text.strip()

                        # 寫入標題、時間
                        writer.writerow([title, like_and_dislike, date])
                    else:
                        print(f"爬取失敗")
                else:
                    print(
                        f"沒有找到標題的連結: {article.find('div', class_='title').text.strip()}")
            except Exception as e:
                print(f"爬取失敗: {e}")

        # 找到上一頁的按鈕，繼續下一頁的爬取
        prev_page_link = soup.find(
            "div", class_="btn-group-paging").find_all("a")
        if len(prev_page_link) > 1:
            prev_page = prev_page_link[1]["href"]
            URL = "https://www.ptt.cc" + prev_page
