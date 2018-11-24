from urllib.request import * 

###open a url
response = urlopen("https://www.ynet.co.il/home/0,7340,L-8,00.html")
print(response)

###http.client.HTTPResponse object
"""
An HTTPResponse instance wraps the HTTP response from the server.
It provides access to the request headers and the entity body.
The response is an iterable object and can be used in a with statement.
"""
#print(dir(response))

###basic response attributes
###http version
print(response.version)
###request url
print(response.url)
###response status code
print(response.status)
###response msg
print(response.msg)

###response headers
print(response.getheaders())


###response  message-body
msg_body = response.read(2000)
#msg_body = response.read(1000).decode("utf-8")
print(msg_body)
print(type(msg_body))













