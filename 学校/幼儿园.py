from time import sleep

from requests_html import HTMLSession

url_str = "http://xuexiao.51sxue.com/slist/?o=&t=1&areaCodeS=4301&level=&sp=&score=&order=&areaS=%%B3%%A4%%C9%%B3%%CA%%D0&searchKey=&page=%d"
name_str = '//*[@id="dsadas"]/@title'
address_str = '//*[@id="list%d"]/div/div[2]/li[2]/b/text()'
property_str = '//*[@id="list%d"]/div[1]/div[2]/li[3]/b/text()'
nature_str = '//*[@id="list%d"]/div/div[2]/li[4]/ol[1]/b/text()'
class_str = '//*[@id="list%d"]/div[1]/div[2]/li[4]/ol[2]/b/text()'
detail_address_str = '//*[@id="list%d"]/ul/li[1]/b/text()'
phone_str = '//*[@id="list%d"]/ul/li[2]/b/text()'
if __name__ == '__main__':
    session = HTMLSession()

    for j in range(1, 39):
        resp = session.get(url_str % j)
        for i in range(1, 11):
            try:
                name = resp.html.xpath('//*[@id="dsadas"]/@title')[i - 1]
                address = resp.html.xpath(address_str % i)
                proper = resp.html.xpath(property_str % i)
                nature = resp.html.xpath(nature_str % i)
                clazz = resp.html.xpath(class_str % i)
                detail_address = resp.html.xpath(detail_address_str % i)
                phone = resp.html.xpath(phone_str % i)
                with open("长沙幼儿园.csv", "a+") as yuhua_csv:
                    yuhua_csv.write(
                        name + "," + str(address) + "," + str(proper) + "," + str(nature) + "," + str(clazz) + "," +
                        str(detail_address) + "," + str(phone) + "\n")
            except Exception as e:
                print(e)
            finally:
                if yuhua_csv != None:
                    yuhua_csv.close()
        print("已经爬到第 " + str(j) + " 页了")
        sleep(2)
