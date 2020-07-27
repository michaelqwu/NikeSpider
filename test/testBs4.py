from bs4 import BeautifulSoup

file = open("./baidu.html","rb")

html = file.read()
bs = BeautifulSoup(html, "html.parser")

print(bs.title)