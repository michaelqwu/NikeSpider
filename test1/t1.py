import requests


url = 'https://www.adidas.co.uk/stan_smith/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
headers = {'User-Agent': user_agent}

r = requests.get(url, headers=headers)

print(r.content)