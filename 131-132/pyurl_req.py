from urllib.request import * 

#####create request
#####(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
##request = Request("https://www.ynet.co.il/home/0,7340,L-8,00.html")
##
##print(request)
##print(dir(request))
##
#####request attributes
#####The URI scheme
##print(request.type)
#####The original URL
##print(request.full_url)
#####The host
##print(request.host)
#####request selector
##print(request.selector)
#####request method
##print(request.get_method())
#####request header_items
##print(request.header_items())


from urllib.parse import urlencode, urlparse, urlunparse

##url = "https://www.act.co.il/index.php"
##queryData = {"action":"item", "nid":"1829", "t":"5"}


url= "https://www.homeless.co.il/rent/inumber1=2"




##url = "https://www.google.co.il/search"
##queryData = {"q":"python"}
headers = {}
headers["User-Agent"] = "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)"

##d = urlencode(queryData)

##request = Request(url + '?' + d)
##request = Request(url + '?' + d, headers = headers)

request = Request(url, headers = headers)

print(request.full_url)
response = urlopen(request)
resData = response.read()

print(type(resData))


with open("te0.html", "wb") as f:
      f.write(resData)

##print(resData)
















