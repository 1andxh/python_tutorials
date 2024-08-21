from urllib import request

url = 'https://www.google.com/search?q=python%20web%20scraping%20tutorial'
page = request.urlopen(url)

status = page.code
print(type(page))
print(status)
