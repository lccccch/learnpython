import urllib2
# response = urllib2.urlopen('http://wwww.baidu.com')
# html = response.read()
# print html


request = urllib2.Request("http://www.baidu.com")
response2 = urllib2.urlopen(request)
html2 = response2.read()
print html2