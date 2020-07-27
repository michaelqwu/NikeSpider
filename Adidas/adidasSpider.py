import sys
from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt
import sqlite3

def main():
    name = "white shoes"
    urlName = urllib.parse.quote(name)
    baseurl = "https://www.adidas.com/us/search?q="+urlName
    print(baseurl)
    datalist = getData(baseurl)

    savepath = name + ".xls"
    saveData(datalist,savepath)



def getData(baseurl):
    datalist = []
    # for i in range (0,10):
    #     url = baseurl + str(i*25)
    #     html = askURL(url)
    html = askURL(baseurl)
    soup = BeautifulSoup(html,"html.parser")
    for item in soup.find_all('div',class_="grid-item___eaXVb"):
        # print(item)
        # break
        data = []
        item = str(item)
        findLink = re.compile(r'href="(.*?)">')
        link = re.findall(findLink,item)[0]  #re to find the link
        # print(link)
        findName = re.compile(r'<span class="gl-label gl-label--m gl-label--condensed gl-product-card__name" title=.*>(.*?)</span>')

        itemName = re.findall(findName,item)[0]
        # print(itemName)
        findImgLink = re.compile(r'<img data-auto-id="image" title=.* src="(.*?)"')
        # itemImg = re.findall(findImgLink,item)[0]
        # print(itemImg)
        findPrice = re.compile(r'="<span class="gl-price__value">(.*?)</')
        itemPrice = re.findall(findPrice,item)[0]
        # print(itemPrice)
        data.append(link)
        data.append(itemName)
        data.append(itemPrice)
        datalist.append(data)

    print(datalist)
    return datalist



def askURL(url):
    head = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    request = urllib.request.Request(url)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

def saveData(datalist,savepath):
    workbook = xlwt.Workbook(encoding="utf-8",style_compression=0)
    worksheet = workbook.add_sheet('nike',cell_overwrite_ok=True)
    col = ("link","item name","tiem price")
    for i in range(0,3):
        worksheet.write(0,i,col[i])
    for i in range(0,24):
        data = datalist[i]
        for j in range(0,3):
            worksheet.write(i+1,j,data[j])
    workbook.save(savepath)


if __name__ == "__main__":
    main()

