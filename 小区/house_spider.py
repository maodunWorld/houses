from requests_html import HTMLSession
from time import sleep

name_str = '//*[@id="list-content"]/div[%d]/div[1]/h3/a/@title'
address_str = '//*[@id="list-content"]/div[%d]/div[1]/address/text()'

url_str = 'https://cs.anjuke.com/community/xingshac/p%d/'

if __name__ == '__main__':
    session = HTMLSession()

    for j in range(1, 13):
        r = session.get(url_str % j)
        for i in range(2, 32):
            try:
                name = r.html.xpath(name_str % i)[0].strip()
                addr = r.html.xpath(address_str % i)[0].strip()
                print(name + addr)
                with open("长沙县.csv", "a+") as yuhua_csv:
                    yuhua_csv.write(name + "," + addr + "\n")
            except Exception as e:
                print(e)
            finally:
                if yuhua_csv != None:
                    yuhua_csv.close()
        print("已经爬到第 " + str(j) + " 页了")
        sleep(20)
