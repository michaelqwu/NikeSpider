import  urllib.request

#response = urllib.request.urlopen("http://www.nike.com")
#print(response.read().decode('utf-8'))

# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding = "utf-8")
# post = urllib.request.urlopen("http://httpbin.org/post", data = data)
# print(post.read().decode("utf-8"))

# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=1)
#     print(response.read().decode("utf-8"))
#
# except urllib.error.URLError as e:
#     print("time out!")
#
# response = urllib.request.urlopen("http://nike.com",timeout=10)
# print(response.getheaders())

url = "http://adidas.com/us"
headers = {'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'}

data = bytes(urllib.parse.urlencode({'name' : 'eric'}),encoding = "utf-8")
req = urllib.request.Request(url = url,data = data, headers = headers, method="POST")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))