from time import sleep

from requests_html import HTMLSession

url_str = "https://www.donghetea.com/quotes.php?id=7&price_min=0&price_max=0&page=%d&sort=shop_price&order=desc"
name_js = 'body > div.block.clearfix > div.quotes_item > ul > li:nth-child(%d) > span.dh1 > a'
price_js = 'body > div.block.clearfix > div.quotes_item > ul > li:nth-child(%d) > span.dh2'
incre_js = 'body > div.block.clearfix > div.quotes_item > ul > li:nth-child(%d) > span.dh3 > span'
incre_per_js = 'body > div.block.clearfix > div.quotes_item > ul > li:nth-child(%d) > span.dh4 > span'
year_js = 'body > div.block.clearfix > div.quotes_item > ul > li:nth-child(%d) > span.dh5'
update_js = 'body > div.block.clearfix > div.quotes_item > ul > li:nth-child(%d) > span.dh6'
score_js = 'body > div.block.clearfix > div.quotes_item > ul > li:nth-child(%d) > span.dh7 > div.gc_fen'
num_js = 'body > div.block.clearfix > div.quotes_item > ul > li:nth-child(%d) > span.dh7 > div.gc_num > em'

if __name__ == '__main__':
    session = HTMLSession()

    for j in range(1, 19):
        resp = session.get(url_str % j)
        for i in range(1, 29):
            try:
                name = resp.html.find(name_js % i, first=True).text
                price = resp.html.find(price_js % i, first=True).text
                incre = resp.html.find(incre_js % i, first=True).text
                incre_per = resp.html.find(incre_per_js % i, first=True).text
                year = resp.html.find(year_js % i, first=True).text
                update = resp.html.find(update_js % i, first=True).text
                score = resp.html.find(score_js % i, first=True).text
                num = resp.html.find(num_js % i, first=True).text
                with open("茶叶.csv", "a+", encoding="utf8") as yuhua_csv:
                    yuhua_csv.write(
                        name + "," + price + "," + incre + "," + incre_per + "," + year + "," +
                        update + "," + score + "," + num + "\n")
            except Exception as e:
                print(e)
            finally:
                if yuhua_csv != None:
                    yuhua_csv.close()
        print("已经爬到第 " + str(j) + " 页了")
        sleep(2)
